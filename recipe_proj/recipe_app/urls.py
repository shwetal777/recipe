from django.urls import path

from django.contrib.auth.views import LoginView, LogoutView

from recipe_app.views import (
    RecipeCreateView,
    RecipeDeleteView,
    RecipeUpdateView,
    log_rating,
    create_shopping_item,
    RecipeDetailView,
    RecipeListView,
    signup
)

urlpatterns = [
    path("", RecipeListView.as_view(), name="recipes_list"),
    path("<int:pk>/", RecipeDetailView.as_view(), name="recipe_detail"),
    path("<int:pk>/delete/", RecipeDeleteView.as_view(), name="recipe_delete"),
    path("new/", RecipeCreateView.as_view(), name="recipe_new"),
    path("<int:pk>/edit/", RecipeUpdateView.as_view(), name="recipe_edit"),
    path("<int:recipe_id>/ratings/", log_rating, name="recipe_rating"),
    path("shopping_items/create", create_shopping_item, name="shopping_item_create"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("signup/", signup, name="signup"),
    # path("shopping_items/delete", delete_all_shopping_items, name="delete_all_shopping_items"),
    # path("shopping_items/", ShoppingItemListView.as_view(), name="shopping_items_list"),
]

