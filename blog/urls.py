from django.urls import path

from blog.views import index, ola #nesta linha importamos as functions views.

urlpatterns = [
    path('index/', index, name = "index"), #defina a rota /index
    path('ola/', ola, name="ola") #Define a rota /ola
]