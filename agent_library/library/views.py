from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .agents.agent_functions import get_llm_recommendation
# Create your views here.

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def get_books(request):
    print("Called")
    print("Query params:", request.GET)  # Debug
    genre = request.GET.get('genre', '')
    
    recommendations = get_llm_recommendation(genre)

    return JsonResponse({"books" : recommendations['recommendations']})
