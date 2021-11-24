from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Categories (models.Model):
    name = models.CharField(verbose_name='Name',
                            blank=False, null=False, max_length=50)

    description = models.TextField(verbose_name='Description',
                                   blank=False, null=False, max_length=200)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Courses (models.Model):
    title = models.CharField(verbose_name='Title',
                             blank=False, null=False, max_length=50)

    description = models.TextField(verbose_name='Description',
                                   blank=False, null=False, max_length=200)

    price = models.FloatField(verbose_name='Price', blank=False, null=False)

    image = models.ImageField(verbose_name='Image',
                              upload_to='Courses', null=True, blank=True)

    category = models.ForeignKey(
        Categories, on_delete=models.CASCADE, verbose_name='Category')

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Author')

    created = models.DateTimeField(verbose_name='Created', auto_now_add=True)

    updated = models.DateTimeField(verbose_name='Updated', auto_now_add=True)

    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'

    def __str__(self):
        return self.title
