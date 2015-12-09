from django.contrib import admin
from main.models import Recipe, CustomUser, Ingredient

# Register your models here.
admin.site.register(Recipe)
admin.site.register(CustomUser)
admin.site.register(Ingredient)