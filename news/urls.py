from django.urls import path
from .views import home, category

urlpatterns = [
    path("home/", home),
    path("category/<str:category>/", category),
]
