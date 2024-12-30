import jdatetime
from django.db import models
from user_module.models import User


class BlogModel(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    image = models.ImageField(upload_to='blog', verbose_name='تصویر')
    text = models.TextField(verbose_name='متن')
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, verbose_name='کاربر')
    date = models.DateTimeField(blank=True, null=True, verbose_name='تاریخ')
    is_active = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')

    def __str__(self):
        return self.title

    def get_date_fa(self):
        date_fa = jdatetime.GregorianToJalali(self.date.year, self.date.month, self.date.day)
        final_date = date_fa.getJalaliList()
        return f'{final_date[0]}/{final_date[1]}/{final_date[2]}'

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'
