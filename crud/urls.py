from django.urls import path, include

from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.IndexPageView.as_view(), name='index'),
    path('generic/', views.GenericPageView.as_view(), name='generic'),
    path('forum/', views.ElementsPageView.as_view(), name='forum'),
    path('categories/', views.CategoriesListView.as_view(), name='categories_list'),
    path('category/<int:pk>/', views.CategoryDetailView.as_view(), name='category'),
    path('create/', views.RecipeCreateView.as_view(), name='recipe_create'),
    path('edit/<int:pk>/', views.RecipeEditView.as_view(), name='recipe_edit'),
    path('delete/<int:pk>/', views.RecipeDeleteView.as_view(), name='recipe_delete'),
    path('<int:pk>/', views.RecipeDetailView.as_view(), name='recipe_detail'),
    path('search-results/', views.SearchResultsView.as_view(), name='search_results')
]
