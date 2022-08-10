from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('foods/', views.food_index, name='foods_index'),
  path('foods/<int:dog_id>/', views.food_detail, name='foods_detail'),
  path('foods/create/', views.FoodCreate.as_view(), name="foods_create"),
  path('foods/<int:pk>/update/', views.FoodUpdate.as_view(), name='foods_update'),
  path('foods/<int:pk>/delete/', views.FoodDelete.as_view(), name='foods_delete'),
  path('accounts/signup/', views.signup, name='signup'),
  path('meals/create/', views.MealCreate.as_view(), name='meals_create'),
  path('meals/<int:pk>/', views.MealDetail.as_view(), name='meals_detail'),
  path('meals/', views.MealList.as_view(), name='meals_index'),
  path('meals/<int:pk>/update/', views.MealUpdate.as_view(), name='meals_update'),
  path('meals/<int:pk>/delete/', views.MealDelete.as_view(), name='meals_delete'),
  path('dogs/<int:dog_id>/assoc_meal/<int:meal_id>/', views.assoc_meal, name='assoc_meal'),
]