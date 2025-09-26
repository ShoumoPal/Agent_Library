from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, StreamingHttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .agents.agent_functions import get_llm_recommendation, stream_summary
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

@csrf_exempt
def stream_book_summary_view(request):
    if request.method == "POST":
        import json
        data = json.loads(request.body)
        title = data.get("title", "")
        if not title:
            return StreamingHttpResponse("data: No title provided\n\n", content_type="text/event-stream", status=400)

        def event_stream():
            for chunk in stream_summary(title):
                # SSE format: data: <text>\n\n
                yield f"data: {chunk}\n\n"

        return StreamingHttpResponse(event_stream(), content_type="text/event-stream")
    return StreamingHttpResponse("data: Invalid request\n\n", content_type="text/event-stream", status=400)