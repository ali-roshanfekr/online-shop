from django.db import models

# Create your models here.

class SliderModel(models.Model):
    image = models.ImageField(upload_to='./slider')
    is_active = models.BooleanField(default=False)


class LogoModel(models.Model):
    image = models.ImageField(upload_to='./logo')
    is_active = models.BooleanField(default=False)
