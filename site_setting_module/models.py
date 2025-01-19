from django.db import models


class SliderModel(models.Model):
    image = models.ImageField(upload_to='./slider', verbose_name='تصویر')
    is_active = models.BooleanField(default=False, verbose_name='فعال/غیرفعال')

    class Meta:
        verbose_name = 'پوستر'
        verbose_name_plural = 'پوستر ها'


class LogoModel(models.Model):
    image = models.ImageField(upload_to='./logo', verbose_name='تصویر')
    is_active = models.BooleanField(default=False, verbose_name='فعال/غیرفعال')

    class Meta:
        verbose_name = 'لوگو'
        verbose_name_plural = 'لوگو ها'


class LinkModel(models.Model):
    title = models.CharField(max_length=300, null=True, verbose_name='عنوان')
    link = models.CharField(max_length=300, verbose_name='لینک')
    is_active = models.BooleanField(default=False, verbose_name='فعال/غیرفعال')
    image = models.ImageField(upload_to='link', null=True, blank=True, verbose_name='تصویر')

    class Meta:
        verbose_name = 'لینک'
        verbose_name_plural = 'لینک ها'
