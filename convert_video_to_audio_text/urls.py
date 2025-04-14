"""Определяет схемы URL для learning_logs."""

from django.urls import path
from . import views

app_name = 'convert_video_to_audio_text'
urlpatterns = [
    # Домашняя страница
    path('', views.audio_function, name='audio_function'),
]
