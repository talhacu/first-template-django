from django.urls import path
from . import views

urlpatterns = [
    path("lan/", views.ornekep, name="orneq"),
    path("sick/", views.keepgoing, name="sick")

]
