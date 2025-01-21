from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('tanishq/',views.tanishq),
    path('mudra/',views.mudra),
    path('send/tanishq', views.send_tanishq, name='send_tanishq'),
    path('send/mudra', views.send_mudra, name='send_mudra'),
    path('chat/', views.get_chat_messages, name='get_chat_messages'),
]
