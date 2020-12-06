from django.contrib import admin

# Register your models here.
from .models import clMenuCategory, clMenuPos, clIngredient, clUnit, clIngrMenuPos

admin.site.register(clMenuCategory)
admin.site.register(clMenuPos)
admin.site.register(clIngredient)
admin.site.register(clUnit)
admin.site.register(clIngrMenuPos)
