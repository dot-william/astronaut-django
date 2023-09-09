from django.urls import path
from . import views

urlpatterns = [
    path("", views.apply, name="index"),
    path('result/', views.submit, name='submit-form'),
]