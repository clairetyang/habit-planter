from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'coloring/index.html')

def home(request):
    return render(request, 'coloring/home.html')

def rec_relaxed(request):
    return render(request, 'coloring/rec_relaxed.html')

def rec_creative(request):
    return render(request, 'coloring/rec_creative.html')

def color_relaxed(request):
    return render(request, 'coloring/color_relaxed.html')

def color_relaxed_panda(request):
    return render(request, 'coloring/color_relaxed_panda.html')

def color_creative(request):
    return render(request, 'coloring/color_creative.html')
    
def color_creative_triangles(request):
    return render(request, 'coloring/color_creative_triangles.html')

def info(request):
    return render(request, 'coloring/info.html')
