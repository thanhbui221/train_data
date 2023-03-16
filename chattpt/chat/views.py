from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.views.generic import TemplateView

class ChatView(TemplateView):
    template_name: str = "chat/chat.html"

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

