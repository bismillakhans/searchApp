
from django.urls import path
from esearch import views

urlpatterns = [
             path('', views.search_index),
]
