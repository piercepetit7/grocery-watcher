from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User



# Create your models here.
class Meal(models.Model):
  name = models.CharField(max_length=50)
  meal_time = models.CharField(max_length=20)
  meal_ingredients = models.CharField(max_length=150)
  day_of_week = models.CharField(max_length=30)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse("meals_detail", kwargs={"pk": self.id})


