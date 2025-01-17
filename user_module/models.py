import jdatetime
from django.contrib.auth.models import AbstractUser
from django.db import models


class StateModel(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'استان'
        verbose_name_plural = 'استان ها'


class CityModel(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    state = models.ForeignKey(StateModel, on_delete=models.CASCADE, verbose_name='استان')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'شهر'
        verbose_name_plural = 'شهر ها'


class User(AbstractUser):
    phone = models.CharField(max_length=300, verbose_name='شماره تلفن')
    active_code = models.CharField(max_length=10)
    token = models.CharField(max_length=100)
    city = models.ForeignKey(CityModel, on_delete=models.PROTECT, null=True, blank=True, verbose_name='شهر')
    address = models.CharField(max_length=300, null=True, verbose_name='آدرس')
    postcode = models.CharField(max_length=300, null=True, blank=True, verbose_name='کد پستی')
    image = models.ImageField(upload_to='user', null=True, blank=True, verbose_name='تصویر')

    def __str__(self):
        return self.username

    def get_date_fa(self):
        date_join_fa = jdatetime.GregorianToJalali(self.date_joined.year, self.date_joined.month, self.date_joined.day)
        final_date_join = date_join_fa.getJalaliList()
        return f'{final_date_join[0]}/{final_date_join[1]}/{final_date_join[2]}'

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'
