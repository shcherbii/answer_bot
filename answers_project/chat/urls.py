from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('room/', views.chat_room, name='chat_room'),
    path('get_chat_response/', views.get_chat_response, name='get_chat_response'),
]