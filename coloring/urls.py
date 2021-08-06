from django.urls import path
from . import views

urlpatterns = [
    # path('demo', views.index, name='demo'),
    # path('new_interaction', views.index, name='new_interaction'),
    path('', views.home, name='home'),
    path('color_relaxed', views.color_relaxed, name='color_relaxed'),
    path('color_relaxed_panda', views.color_relaxed_panda, name='color_relaxed_panda'),
    path('color_creative', views.color_creative, name='color_creative'),
    path('color_creative_triangles', views.color_creative_triangles, name='color_creative_triangles'),
    path('rec_relaxed', views.rec_relaxed, name='rec_relaxed'),
    path('rec_creative', views.rec_creative, name='rec_creative'),
    path('info', views.info, name='info')

]
