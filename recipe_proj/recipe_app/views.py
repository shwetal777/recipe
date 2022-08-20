from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from recipe_app.forms import RatingForm

from recipe_app.models import Recipe, Ingredient, ShoppingItem

class RecipeListView(ListView):
    model = Recipe
    template_name = "list.html"
    paginate_by = 2


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "detail.html"

    # Optional: change context data dictionary
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rating_form"] = RatingForm()

        foods = []
        for item in self.request.user.shopping_items.all():
            foods.append(item.food_item)

        context["servings"] = self.request.GET.get("servings")

        context["food_in_shopping_list"] = foods
        return context


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = "new.html"
    fields = ["name", "servings", "description", "image"]
    success_url = reverse_lazy("recipes_list")

    # Optional: overwrite form data (before save)
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipe
    template_name = "edit.html"
    fields = ["name", "servings", "description", "image"]
    success_url = reverse_lazy("recipes_list")


class RecipeDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipe
    template_name = "delete.html"
    success_url = reverse_lazy("recipes_list")


from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.db import IntegrityError

# Create your views here.
def log_rating(request, recipe_id):
    if request.method == "POST":
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            try:
                rating.recipe = Recipe.objects.get(pk=recipe_id)
            except Recipe.DoesNotExist:
                return redirect("recipes_list")
            rating.save()
    return redirect("recipe_detail", pk=recipe_id)


def create_shopping_item(request):
    ingredient_id = request.POST.get("ingredient_id")

    ingredient = Ingredient.objects.get(id=ingredient_id)

    user = request.user

    try:
        ShoppingItem.objects.create(
            food_item=ingredient.food,
            user=user,
        )
    except IntegrityError:
        pass  

    return redirect("recipe_detail", pk=ingredient.recipe.id)


from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password1")
            user = User.objects.create_user(
                username=username,
                password=password,
            )
            user.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()
    context = {
        "form": form,
    }
    return render(request, "registration/signup.html", context)