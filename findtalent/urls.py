from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('results', views.results),
    path('add', views.save_to_db)
]