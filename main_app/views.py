from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Food, Meal
from .forms import FeedingForm

# Create your views here.
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def food_index(request):
  food = Food.objects.filter(user=request.user)
  return render(request, 'food/index.html', { 'food': food })

@login_required
def food_detail(request, food_id):
  food = Food.objects.get(id=food_id)
  meals_food_doesnt_have = Meal.objects.exclude(id__in = food.meals.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'food/detail.html', {
    'food': food, 'feeding_form': feeding_form, 'meals': meals_food_doesnt_have
  })

class FoodCreate(LoginRequiredMixin, CreateView):
  model = Food
  fields = ['name', 'type', 'description', 'expiration']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class FoodUpdate(LoginRequiredMixin, UpdateView):
  model = Food
  fields = ['type', 'description', 'expiration']

class FoodDelete(LoginRequiredMixin, DeleteView):
  model = Food
  success_url = '/food/'

@login_required
def add_feeding(request, food_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.food_id = food_id
    new_feeding.save()
  return redirect('food_detail', food_id=food_id)

class MealCreate(LoginRequiredMixin, CreateView):
  model = Meal
  fields = '__all__'

class MealList(LoginRequiredMixin, ListView):
  model = Meal

class MealDetail(LoginRequiredMixin, DetailView):
  model = Meal

class MealUpdate(LoginRequiredMixin, UpdateView):
  model = Meal
  fields = ['name', 'color']

class MealDelete(LoginRequiredMixin, DeleteView):
  model = Meal
  success_url = '/meals/'

@login_required
def assoc_meal(request, food_id, meal_id):
  Food.objects.get(id=food_id).meals.add(meal_id)
  return redirect('food_detail', food_id=food_id)

def signup(request):
  error_message = ""
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('food_index')
    else:
      error_message = "Invalid sign up - try again"
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)