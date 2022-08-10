from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User



# Create your models here.
class Meal(models.Model):
  name = models.CharField(max_length=50)
  type = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse("meals_detail", kwargs={"pk": self.id})

class Food(models.Model): 
  name = models.CharField(max_length=100)
  type = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  expiration = models.IntegerField()
  meals = models.ManyToManyField(Meal)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('foods_detail', kwargs={'food_id': self.id})

