# from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db import models

class CathegoryModel(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.title}'

class RecipeModel(models.Model):
    COMPLEXITY = [
        ('easy', 'easy'),
        ('medium', 'medium'),
        ('complex', 'complex'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    cooking =  models.TextField()
    time = models.CharField(max_length=20)
    image = models.ImageField()
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    cathegories = models.ManyToManyField(CathegoryModel, default='new')
    complexity = models.CharField(max_length = 10, choices=COMPLEXITY)

    def __str__(self):
        return f'{self.title}'
    


class RecipeToCategoryModel(models.Model):
    recipe = models.ForeignKey(RecipeModel, on_delete=models.CASCADE)
    cathegory = models.ForeignKey(CathegoryModel, on_delete=models.CASCADE)
    date_added = models.DateField(auto_now_add=True)

