from django.urls import path
from . import views

urlpatterns = [
    path('put_sequence/', views.put_sequence),
]