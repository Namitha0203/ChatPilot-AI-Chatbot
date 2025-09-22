

from django.urls import path
from .views import chat_view, home, history_view

urlpatterns = [
    path('', home, name='homepage'),           # ✅ Homepage at /
    path('chat/', chat_view, name='chat'),     # Chatbot
    path('history/', history_view, name='history'),  # Chat history
]



