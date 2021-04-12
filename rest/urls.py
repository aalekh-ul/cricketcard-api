
from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from crick import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('players/',views.playerlist.as_view()),
    path('random/',views.random_playerlist.as_view()),



]
