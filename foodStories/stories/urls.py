from django.urls import path
from stories import views

urlpatterns = [
    path('', views.home, name='home' ),
    path('about/', views.about, name='about' ),
    path('stories/', views.stories, name='stories' ),
    path('recipes/', views.recipes, name='recipes' ),
    path('contact/', views.contact, name='contact' ),
]