from django.urls import path
from . import views

urlpatterns = [
    path('get_sequence_logo/', views.get_sequence_logo),
]