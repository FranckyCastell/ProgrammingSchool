from django.db import models

# Create your models here.


class Event (models.Model):
    title = models.CharField(verbose_name='Título',
                             max_length=50, blank=True, null=True)

    start = models.CharField(verbose_name='Data Inicio',
                             blank=True, null=True, default='2021-12-11T22:30:00', max_length=20)

    end = models.CharField(verbose_name='Data Final',
                           blank=True, null=True, default='2021-12-11T22:30:00', max_length=20)

    url = models.URLField(verbose_name='URL Google Meet',
                          blank=True, null=True)

    class Meta:
        verbose_name = 'event'
        verbose_name_plural = 'events'

    def __str__(self):
        return self.title
