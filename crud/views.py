from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.db.models import Q

from .models import Recipe, Category

class CategoryView(generic.ListView):
    model = Category
    template_name = 'base.html'


class CategoryDetailView(generic.DetailView):
    model = Category
    template_name = 'recipes/category_detail.html'
    context_object_name = 'category'


class CategoriesListView(generic.ListView):
    model = Category
    template_name = 'recipes/categories_list.html'



class IndexPageView(generic.ListView):
    model = Recipe
    template_name = 'index.html'
    context_object_name = 'recipes'
    paginate_by = 3
    queryset = Recipe.objects.all()


class GenericPageView(TemplateView):
    template_name = 'generic.html'


class ElementsPageView(TemplateView):
    template_name = 'elements.html'


class RecipeDetailView(generic.DetailView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html'
    context_object_name = 'recipe'


    def count_views(self):
        obj = super().get_object(pk=self.pk)
        obj.views += 1
        obj.save()
        return obj



class RecipeCreateView(generic.CreateView):
    model = Recipe
    template_name = 'recipes/recipe_create.html'
    fields = '__all__'
    success_url = reverse_lazy('recipes:recipe_list')


class RecipeEditView(generic.UpdateView):
    model = Recipe
    template_name = 'recipes/recipe_edit.html'
    fields = ('title', 'description', 'author', 'image')
    context_object_name = 'recipe'

    def get_success_url(self):
        return reverse_lazy(
            'recipes:recipe_detail',
            kwargs={'pk': self.object.pk}
        )

class RecipeDeleteView(generic.DeleteView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html'
    success_url = reverse_lazy('recipes:recipe_delete')


class SearchResultsView(generic.ListView):
    model = Recipe
    template_name = 'recipes/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Recipe.objects.filter(title__icontains=query)
        return object_list


