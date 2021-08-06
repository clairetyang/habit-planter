from django.urls import path
from . import views

urlpatterns = [
    # path('demo', views.index, name='demo'),
    # path('new_interaction', views.index, name='new_interaction'),
    path('', views.home, name='home'),
    path('habit_tree', views.habit_tree, name='habit_tree'),
    path('color_creative', views.color_creative, name='color_creative'),
    path('rec_relaxed', views.rec_relaxed, name='rec_relaxed'),
    path('rec_creative', views.rec_creative, name='rec_creative'),
    path('info', views.info, name='info')

]
