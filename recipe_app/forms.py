from django import forms
#from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import RecipeModel, CathegoryModel, RecipeToCategoryModel
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    pass

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

# class CustomUserChangeForm(UserChangeForm):
#     class Meta:
#         model = CustomUser
#         fields = ('username', 'email', 'status')

class RecipeForm(forms.ModelForm):
    class Meta:
        model = RecipeModel
        fields = ('title', 'description', 'cooking', 'time', 'image', 'cathegories', 'complexity')

class CathegoryForm(forms.ModelForm):
    class Meta:
        model = CathegoryModel
        fields = ('title',)

class RecipeToCathegoryForm(forms.ModelForm):
    model = RecipeToCategoryModel
    fields = ()

