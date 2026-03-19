from django.shortcuts import render

# Create your views here.


def home(request):
    context = {"title": "Pagina Principal "}
    return render(request, "home/index.html", context)
