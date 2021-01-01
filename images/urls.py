from django.urls import path
from . import views

urlpatterns = [
    path('imgtopdf', views.imgtopdf),
]
