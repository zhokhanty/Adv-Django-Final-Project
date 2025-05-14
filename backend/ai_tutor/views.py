from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .tasks import process_ai_message, generate_similar_task, analyze_code
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .mongo import chat_collection

class AskAITutorView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        question = request.data.get('question')
        context = request.data.get('context', '')
        user_id = str(request.user.id)

        task = process_ai_message.delay(user_id, question, context)
        return Response({"message": "AI is processing your question", "task_id": task.id})
    

class GenerateSimilarTaskView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        original_problem = request.data.get('problem')
        user_id = str(request.user.id)

        task = generate_similar_task.delay(user_id, original_problem)
        return Response({
            "message": "Генерация аналогичной задачи запущена",
            "task_id": task.id
        })

class AnalyzeCodeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        code = request.data.get("code")
        if not code:
            return Response({"error": "Необходимо передать поле 'code'"}, status=400)

        user_id = str(request.user.id)
        task = analyze_code.delay(user_id, code)

        return Response({
            "message": "Проверка кода запущена",
            "task_id": task.id
        })





class ChatHistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_id = str(request.user.id)
        history = list(chat_collection.find(
            {"user_id": user_id}
        ).sort("created_at", -1))

        for item in history:
            item["_id"] = str(item["_id"])  # преобразуем ObjectId в строку

        return Response(history)

