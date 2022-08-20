from django.db import models
from django.conf import settings

USER_MODEL = settings.AUTH_USER_MODEL


# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=125)
    author = models.ForeignKey(
        USER_MODEL,
        related_name="recipes",
        on_delete=models.CASCADE,
        null=True,
    )
    description = models.TextField()
    image = models.URLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    servings = models.PositiveSmallIntegerField(null=True)

    def __str__(self):
        return f"{self.name} by {self.author}"

class Step(models.Model):
    recipe = models.ForeignKey(
        "Recipe",
        related_name="steps",
        on_delete=models.CASCADE,
    )
    order = models.PositiveSmallIntegerField()
    directions = models.CharField(max_length=300)
    food_items = models.ManyToManyField("FoodItem", blank=True)

    def __str__(self):
        return f"{self.order} {self.directions}"


class Rating(models.Model):
    value = models.IntegerField(blank=True)

    def __str__(self):
        return f"{self.value}"


class Ingredient(models.Model):
    food = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.food}"


class ShoppingItem(models.Model):
    item = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.item}"


class FoodItem(models.Model):
    item = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.item}"