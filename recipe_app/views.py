from random import choice, randint
from django.shortcuts import get_object_or_404, redirect, render
#from django.urls import reverse_lazy
from .models import RecipeModel, CathegoryModel
from django.contrib.auth.views import LoginView
from .forms import LoginForm, RecipeForm, UserRegistrationForm

from django.contrib.auth import logout
from django.contrib.auth.models import User



def index(request):
    all_recipes = RecipeModel.objects.all()
    recipes_amount = len(all_recipes)
    ids = [i for i in range(1, recipes_amount+1)]
    recipes = []
    for i in range(5):
        number = choice(ids)
        recipes.append(RecipeModel.objects.get(pk=number))
        ids.remove(number)
    context = {'type': 'main', 'recipes': recipes}
    return render(request,'recipe_app/some_recipes.html', context)


class UserLoginView(LoginView):
    form_class = LoginForm
    template_name = 'recipe_app/login.html'


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password, set group
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.set_group('standart_user')
            # Save the User object
            new_user.save()
            return render(request, 'recipe_app/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'recipe_app/register.html', {'user_form': user_form})

def logout_view(request):
    logout(request)
    return redirect(index)

def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return render(request, 'recipe_app/add_recipe.html', {'form': form, 'saved_form': recipe})
        else:
            form = RecipeForm()
    else:
            form = RecipeForm()
    return render(request, 'recipe_app/add_recipe.html', {'form': form})

def edit_recipe(request, recipe_id):
    post = get_object_or_404(RecipeModel, pk=recipe_id)
    if request.method == "POST":
        form = RecipeForm(request.POST, instance=post)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('full_recipe', recipe_id=recipe.pk)
    else:
        form = RecipeForm(instance=post)
    return render(request, 'recipe_app/add_recipe.html', {'form': form})


def full_recipe(request, recipe_id):
    recipe = get_object_or_404(RecipeModel, pk=recipe_id)
    context = {'recipe': recipe}
    return render(request,'recipe_app/full_recipe.html', context)

    
def author_recipes(request, author_id):
    author = get_object_or_404(User, pk=author_id)
    recipes = RecipeModel.objects.filter(author=author)
    context = {'type':author, 'recipes':recipes}
    return render(request, 'recipe_app/some_recipes.html', context)


def cathegory_recipes(request, cathegory_name):
    cathegory = get_object_or_404(CathegoryModel, title=cathegory_name)
    recipes = []
    for recipe in RecipeModel.objects.all():
        for cathegory in recipe.cathegories.all():
            if cathegory.title == cathegory_name:
                recipes.append(recipe)
    context = {'type': cathegory_name, 'recipes': recipes}
    return render(request,'recipe_app/some_recipes.html', context)


def complexity_recipes(request, complexity_rate):
    recipes = RecipeModel.objects.filter(complexity=complexity_rate)
    context = {'type': complexity_rate, 'recipes': recipes}
    return render(request,'recipe_app/some_recipes.html', context)


def random_recipe(request):
    all_recipes = RecipeModel.objects.all()
    number = randint(1, len(all_recipes)) 
    recipe = RecipeModel.objects.get(pk=number)
    context = {'recipe': recipe}
    return render(request,'recipe_app/full_recipe.html', context)


    