from django.db import models

# Create your models here.


class ProgrammingLanguage (models.Model):
    name = models.CharField(verbose_name='Name',
                            blank=False, null=False, max_length=50)

    class Meta:
        verbose_name = 'programmingLanguage'
        verbose_name_plural = 'programmingLanguages'

    def __str__(self):
        return self.name


class Users (models.Model):
    name = models.CharField(verbose_name='Name',
                            blank=False, null=False, max_length=50)

    surname = models.CharField(verbose_name='Surname',
                               blank=False, null=False, max_length=50)

    language = models.ForeignKey(
        ProgrammingLanguage, verbose_name='Programming Language', on_delete=models.CASCADE)

    image = models.ImageField(verbose_name='Image',
                              upload_to='Personal', null=True, blank=True)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.name
