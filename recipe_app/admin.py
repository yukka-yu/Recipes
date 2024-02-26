from django.contrib import admin

#from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from .models import RecipeModel, CathegoryModel

# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = ['email', 'username',]

# class RecipeAdmin():
#     add_form = RecipeCreationForm
#     form = RecipeChangeForm
#     model = RecipeModel
#     list_display = ['email', 'username',]


admin.site.register(RecipeModel) 
admin.site.register(CathegoryModel)
