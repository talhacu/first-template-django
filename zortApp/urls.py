from django.urls import path
from . import views


urlpatterns = [
    path("zort/", views.zirot, name="zirot")
]
