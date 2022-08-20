from django.contrib import admin

from recipe_app.models import Recipe, Step, Rating, FoodItem, ShoppingItem

# Register your models here
# Custom model Admin (admin.py): 
# class BlogAdmin(admin.ModelAdmin)
#     fields = ("title", "description") # Fields to use for add/edit/show page
#     list_display = ("title", "description") # fields to display in search page
#     list_display_links = ("title") # fields that will be a link in search page
#     ordering("date_created",) # Ordering allowed in the search page
#     search_fields("title", "description") # Search fields allowed in the search page

# Register app
admin.site.register(Recipe)
admin.site.register(Step)
admin.site.register(Rating)
admin.site.register(ShoppingItem)
admin.site.register(FoodItem)