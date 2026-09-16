import os

from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        number = request.POST.get("number")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password, number=number)

        if user is not None:
            auth_login(request, user)
            return redirect("home")
        else:
            return render(request, "login.html", {
                "error": "Invalid username or password"
            })

    return render(request, "login.html")


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        number = request.POST.get("number")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            return render(request, "register.html", {
                "error": "Username already exists"
            })

        user = User.objects.create_user(
            username=username,
            email=email,
            number=number,
            password=password
        )

        user.save()

        return redirect("enter")

    return render(request, "register.html")


def home(request):
    return render(request, "home.html")

def enter(request):
    return render(request, "enter.html")


from google import genai
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json
import os
import json

import json
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from google import genai


def ai(request):
    return render(request, "ai.html")


@require_POST
def chat_api(request):
    try:
        data = json.loads(request.body)
        message = data.get("message", "").strip()

        if not message:
            return JsonResponse({"error": "Message is empty"}, status=400)

        print("USER MESSAGE:", message)
        print("GEMINI KEY EXISTS:", bool(settings.GEMINI_API_KEY))

        if not settings.GEMINI_API_KEY:
            return JsonResponse({
                "error": "Gemini API key is missing"
            }, status=500)

        client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

        response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=message
)
        

        print("GEMINI RESPONSE:", response.text)

        return JsonResponse({
            "reply": response.text
        })

    except Exception as e:
        print("🔥 AI ERROR:", repr(e))

        return JsonResponse({
            "error": str(e)
        }, status=500)

from django.shortcuts import render
import json

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST

from google import genai
def ai(request):
    return render(request, "ai.html")