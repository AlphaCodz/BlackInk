from django.shortcuts import render

# Create your views here.
# app_name = "app"

def index(request):
    return render(request, "index.html")

def single(request):
    return render(request, "single.html")