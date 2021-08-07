from django.urls import path
from . import views

urlpatterns = [
    # path('demo', views.index, name='demo'),
    # path('new_interaction', views.index, name='new_interaction'),
    path('title', views.title, name='title'),
    path('home_garden', views.home_garden, name='home_garden'),
    path('survey_name', views.survey_name, name='survey_name'),
    path('survey_focus', views.survey_focus, name='survey_focus'),
    path('survey_goal', views.survey_goal, name='survey_goal'),
    path('survey_steps', views.survey_steps, name='survey_steps'),
    path('habit_tree', views.habit_tree, name='habit_tree'),
    path('butterfly_streak', views.butterfly_streak, name='butterfly_streak'),
    path('butterfly_completion', views.butterfly_completion, name='butterfly_completion'),
    path('send_from', views.send_from, name = 'send_from'),
    path('send_to', views.send_to, name = 'send_to'),
    path('send_to2', views.send_to2, name = 'send_to2'),

]
