from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    imgs = models.ForeignKey('Images', on_delete=models.PROTECT, null=True,
                             verbose_name='Изображения', blank=True)
    description_short = models.TextField(blank=True, verbose_name='Краткое '
                                                                  'описание')
    description_long = models.TextField(blank=True, verbose_name='Полное '
                                                                 'описание')
    lng = models.DecimalField(max_digits=17, decimal_places=14, \
                              verbose_name='Долгота')
    lat = models.DecimalField(max_digits=17, decimal_places=14,
                              verbose_name='Широта')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'
        ordering = ['title']


class Images(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    num = models.IntegerField(verbose_name='Номер')
    image = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True,
                              verbose_name='Изображение')

    def __str__(self):
        return f"{self.num} {self.title}"

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        # ordering = ['-num']
