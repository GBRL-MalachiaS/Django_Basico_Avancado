from django.shortcuts import render

from . import data

# Create your views here.


def home(request):

    context = {"title": "Blog Home ", "posts": data.posts}
    return render(request, "blog/index.html", context)


def post(request, id):
    posts = data.posts
    post = None
    for post in posts:
        if post["id"] == id:
            post = post
            break

    context = {"title": "Post ", "post": post}
    return render(request, "blog/exemplo.html", context)


def exemplo(request):
    context = {"title": "Exemplo "}
    return render(request, "blog/exemplo.html", context)
