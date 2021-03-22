from django.contrib import admin
from . import models

class RecipeAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'author', 'category', 'image')

admin.site.register(models.Recipe, RecipeAdmin)
admin.site.register(models.Author)
admin.site.register(models.Category)