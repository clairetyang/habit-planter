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
    path('habit_tree_1', views.habit_tree_1, name = 'habit_tree_1'),
    path('habit_tree_2', views.habit_tree_2, name = 'habit_tree_2'),
    path('habit_tree_3', views.habit_tree_3, name = 'habit_tree_3'),
    path('habit_tree_4', views.habit_tree_4, name = 'habit_tree_4'),
    path('habit_tree_5', views.habit_tree_5, name = 'habit_tree_5'),
    path('habit_tree_6', views.habit_tree_6, name = 'habit_tree_6'),
    path('habit_tree_7', views.habit_tree_7, name = 'habit_tree_7'),
    path('habit_tree_8', views.habit_tree_8, name = 'habit_tree_8'),
    path('info', views.info, name = 'info'),
    path('menu', views.menu, name = 'menu'),
    path('congratulations', views.congratulations, name = 'congratulations'),
    path('completedgardens', views.completedgardens, name = 'completedgardens'),
    path('completedgardenstitle', views.completedgardenstitle, name = 'completedgardenstitle'),
    path('currentgarden', views.currentgarden, name = 'currentgarden')

]
