from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('', views.endpoint, name ='endpoint'),
    path('all-cocktails/', views.allCocktails, name ='all-cocktails'),
    path('cocktail-detail/<str:pk>/', views.cocktailDetail, name ='cocktail-detail'),
    path('create_cocktail/', views.createCocktail, name ='create_cocktail'),
    path('update-cocktail/<str:pk>/', views.updateCocktail, name ='update-cocktail'),
    path('delete-cocktail/<str:pk>/', views.deleteCocktail, name ='delete-cocktail'),
    path('random-cocktails/', views.randomCocktails, name ='random-cocktails'),
    path('latest-cocktails/', views.latestCocktails, name ='latest-cocktails'),
    path('cocktail-you-created/<str:pk>/', views.cocktailCreator, name ='cocktails-you-created'),
    path('endpoint-cocktails/', views.endpoinLatest10Cocktails, name ='endpoint-cocktails'),
    path('register-user/',views.registerUser, name='register-user'),
    path('login/',obtain_auth_token, name='login')


]