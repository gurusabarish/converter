from django.urls import path
from . import views

urlpatterns = [
    path('', views.imgtopdf, name="imgtopdf"),
    path('jpgtopng', views.jpgtopng),
    path('png', views.png),

]
