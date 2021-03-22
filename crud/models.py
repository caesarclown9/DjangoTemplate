from django.db import models
from django.db.models import Count


class Category(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        ordering = ['title']
        verbose_name_plural = 'categories'

    def __str__(self):
        return f'{self.title}'


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.first_name


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
    image = models.ImageField(blank=True)
    category = models.ManyToManyField(Category, blank=True, null=True, related_name="recipes")
    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} {self.pk}'


