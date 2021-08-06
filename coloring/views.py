from django.shortcuts import render
from django.http import HttpResponse


# def index(request):
#     return render(request, 'coloring/index.html')

def title(request):
    return render(request, 'coloring/title.html')

def home_garden(request):
    return render(request, 'coloring/home_garden.html')

def survey_name(request):
    return render(request, 'coloring/survey_name.html')

def survey_focus(request):
    return render(request, 'coloring/survey_focus.html')

def survey_goal(request):
    return render(request, 'coloring/survey_goal.html')

def survey_steps(request):
    return render(request, 'coloring/survey_steps.html')

def habit_tree(request):
    return render(request, 'coloring/habit_tree.html')

def butterfly_streak(request):
    return render(request, 'coloring/butterfly_streak.html')

def butterfly_completion(request):
    return render(request, 'coloring/butterfly_completion.html')
