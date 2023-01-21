from django.urls import path
from .views import home
from news import views
urlpatterns = [
    path("home/", home),
    path('post/<int:pk>', views.view_post, name="view-post"),
    path('categorie/', views.view_categorie, name="categorie-post"),
]
