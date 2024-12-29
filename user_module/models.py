import jdatetime
from django.contrib.auth.models import AbstractUser
from django.db import models
import jalali_date

# Create your models here.

class User(AbstractUser):
    phone = models.CharField(max_length=20)
    active_code = models.CharField(max_length=10)
    token = models.CharField(max_length=100)

    def __str__(self):
        return self.username

    def get_date_fa(self):
        date_join_fa = jdatetime.GregorianToJalali(self.date_joined.year, self.date_joined.month, self.date_joined.day)
        final_date_join = date_join_fa.getJalaliList()
        return f'{final_date_join[0]}/{final_date_join[1]}/{final_date_join[2]}'

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

