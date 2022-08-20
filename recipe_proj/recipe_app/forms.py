from django import forms

from recipe_app.models import Rating


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ["value"]


# Render form in templates
# <form method="post">
#     {% csrf_token %}
#     {{ form.as_p }}
#     <div class="control">
#       <button class="button">Create</button>
#     </div>
# </form>