from django.shortcuts import render

# Create your views here.


def home(request):
    context = {"title": "Blog Home "}
    return render(request, "blog/index.html", context)


def exemplo(request):
    context = {"title": "Exemplo "}
    return render(request, "blog/exemplo.html", context)
