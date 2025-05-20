from django.http import HttpResponse
from django.shortcuts import render

from todo_app.models import Task


def index(request):
    search_title = request.GET.get('title_filter')
    tasks = Task.objects.filter(name__icontains=search_title) # SELECT * from Tasks

    context = {
         "tasks":tasks,
         "search_title": search_title,
    }

    return render(request, "index.html", context )


    # html_response = [
    #     "<html>",
    #     "<ul>",
    #         "\n".join([f"<li>{t.name} - {t.created_at}</li>"for t in tasks]),
    #     "</ul>",
    #     "</html>",
    # ]
    #
    # return HttpResponse("\n".join(html_response))
