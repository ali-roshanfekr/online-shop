from django.db import models
from user_module.models import User


# Create your models here.

class BlogModel(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to='blog')
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    date = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name: 'مقاله'
        verbose_name_plural: 'مقالات'
