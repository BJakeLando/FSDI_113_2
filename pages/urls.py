from django.urls import path
from posts import views
from .views import (
            AboutView,
            HomeView,
            WeatherPageView
            )

urlpatterns = [
    path('about/', AboutView.as_view(), name= 'about'),
    path('', HomeView.as_view(), name= 'home'),
    path('weather/', WeatherPageView.as_view(), name= 'weather'),

]