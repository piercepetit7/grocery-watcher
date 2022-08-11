from urllib import request
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Meal



# Create your views here.
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')


class MealCreate(LoginRequiredMixin, CreateView):
  model = Meal
  fields = '__all__'
  success_url = '/meals/'

class MealList(LoginRequiredMixin, ListView, request):
  model = Meal.filter(user=request.user)

class MealDetail(LoginRequiredMixin, DetailView):
  model = Meal

class MealUpdate(LoginRequiredMixin, UpdateView):
  model = Meal
  fields = ['name', 'meal_time', 'meal_ingredients', 'day_of_week']
  success_url = '/meals/'

class MealDelete(LoginRequiredMixin, DeleteView):
  model = Meal
  success_url = '/meals/'

def signup(request):
  error_message = ""
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('meals_index')
    else:
      error_message = "Invalid sign up - try again"
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)