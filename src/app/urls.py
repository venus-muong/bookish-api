from django.urls import path

from . import views

urlpatterns = [
    path('visionboard/', views.view_vision_board, name='visionboard')
]