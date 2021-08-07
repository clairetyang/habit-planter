from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('habit_planter/', include('habit_planter.urls')),
]
