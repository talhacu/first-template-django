
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("template_app/",include("template_app.urls")),
    path("ornekApp/", include("ornekApp.urls")),
    path("aboutUS/", include("aboutUS.urls")),
    path("zort/", include("zortApp.urls")),
    path("talha/", include("tahino.urls"))
    

]