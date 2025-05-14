from celery import shared_task
from .openai_service import ask_openai
from .mongo import chat_collection

@shared_task
def process_ai_message(user_id, message_text, context=None):
    messages = [
        {"role": "system", "content": "Ты — AI-наставник. Объясняй просто и понятно."},
        {"role": "user", "content": message_text},
    ]

    if context:
        messages.insert(1, {"role": "user", "content": context})

    answer = ask_openai(messages)

    chat_collection.insert_one({
        "user_id": user_id,
        "question": message_text,
        "answer": answer,
    })

    return answer

@shared_task
def generate_similar_task(user_id, original_problem_description):
    prompt = (
        f"Ты — AI-преподаватель по программированию. "
        f"Пользователь решал задачу: \"{original_problem_description}\".\n"
        f"Сгенерируй аналогичную задачу — немного изменённую, но с той же логикой. "
        f"Сформулируй её чётко, как в олимпиадном задании."
    )

    messages = [{"role": "user", "content": prompt}]
    new_task = ask_openai(messages)

    # Сохраняем в MongoDB
    chat_collection.insert_one({
        "user_id": user_id,
        "type": "generated_task",
        "original": original_problem_description,
        "generated": new_task,
    })

    return new_task

@shared_task
def analyze_code(user_id, user_code):
    prompt = (
        "Ты — опытный Python-разработчик и преподаватель. "
        "Проанализируй код, найди ошибки (если есть), объясни их и предложи исправление. "
        "Вот код:\n\n"
        f"{user_code}"
    )

    messages = [{"role": "user", "content": prompt}]
    analysis = ask_openai(messages)

    # Сохраняем в MongoDB
    chat_collection.insert_one({
        "user_id": user_id,
        "type": "code_analysis",
        "original_code": user_code,
        "analysis": analysis,
    })

    return analysis
