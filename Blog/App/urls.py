from django.urls import path
from .views import *


urlpatterns= [

    path('about/', about, name="About"),
    path('contact/', contact, name="Contact"),
    path('post/', post, name="Post" ),
    path("", inicio, name="Inicio"),

]