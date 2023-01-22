from django.urls import path
from .views import home
from news import views
from .views import home, category

urlpatterns = [
    path("home/", home),
    path("category/<str:category>/", category),
    path('post/<int:pk>', views.view_post, name="view-post"),
    path('category/', views.view_category, name="category-post"),
]
