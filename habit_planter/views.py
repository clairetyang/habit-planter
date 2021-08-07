from django.shortcuts import render
from django.http import HttpResponse


# def index(request):
#     return render(request, 'coloring/index.html')

def title(request):
    return render(request, 'habit_planter/title.html')

def home_garden(request):
    return render(request, 'habit_planter/home_garden.html')

def survey_name(request):
    return render(request, 'habit_planter/survey_name.html')

def survey_focus(request):
    return render(request, 'habit_planter/survey_focus.html')

def survey_goal(request):
    return render(request, 'habit_planter/survey_goal.html')

def survey_steps(request):
    return render(request, 'habit_planter/survey_steps.html')

def habit_tree_1(request):
    return render(request, 'habit_planter/habit_tree_1.html')

def habit_tree_2(request):
    return render(request, 'habit_planter/habit_tree_2.html')

def habit_tree_3(request):
    return render(request, 'habit_planter/habit_tree_3.html')
    
def habit_tree_4(request):
    return render(request, 'habit_planter/habit_tree_4.html')

def butterfly_streak(request):
    return render(request, 'habit_planter/butterfly_streak.html')

def butterfly_completion(request):
    return render(request, 'habit_planter/butterfly_completion.html')
