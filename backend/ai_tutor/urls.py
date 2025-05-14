# ai_tutor/urls.py
from django.urls import path
from .views import AskAITutorView, GenerateSimilarTaskView, AnalyzeCodeView, ChatHistoryView

urlpatterns = [
    path('ask/', AskAITutorView.as_view(), name="ask-ai"),
    path("generate-task/", GenerateSimilarTaskView.as_view(), name="generate-task"),
    path("analyze-code/", AnalyzeCodeView.as_view(), name="analyze-code"),
    path("chat-history/", ChatHistoryView.as_view(), name="chat-history"),
]

