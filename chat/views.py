import os
import requests
from dotenv import load_dotenv
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ChatMessage

# Explicitly load .env from project root (same level as manage.py)
dotenv_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.env')
load_dotenv(dotenv_path)



def home(request):
    return render(request, "chat/home.html")


@login_required
def chat_view(request):
    reply = None

    if request.method == "POST":
        prompt = request.POST.get("prompt")

        # Load API key securely
        api_key = os.environ.get("OPENROUTER_API_KEY")
        if not api_key:
            reply = "API key not found. Please check your .env file."
            return render(request, "chat/chat.html", {"reply": reply})

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        data = {
            "model": "openai/gpt-3.5-turbo",
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        }

        try:
            response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
            result = response.json()

            # Extract reply safely
            reply = result.get("choices", [{}])[0].get("message", {}).get("content", "")
            if not reply:
                reply = "Sorry, the AI did not return a response. Please try again."

            # Save to history
            ChatMessage.objects.create(user=request.user, prompt=prompt, response=reply)

        except Exception as e:
            reply = f"Error: {str(e)}"

    return render(request, "chat/chat.html", {"reply": reply})

@login_required
def history_view(request):
    messages = ChatMessage.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "chat/history.html", {"messages": messages})
