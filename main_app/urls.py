from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('food/', views.food_index, name='food_index'),
  path('food/<int:dog_id>/', views.food_detail, name='food_detail'),
  path('food/create/', views.FoodCreate.as_view(), name="food_create"),
  path('food/<int:pk>/update/', views.FoodUpdate.as_view(), name='food_update'),
  path('food/<int:pk>/delete/', views.FoodDelete.as_view(), name='food_delete'),
]