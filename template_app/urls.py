from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="name"),
    path("talha/", views.tahino, name="name2"),

]
