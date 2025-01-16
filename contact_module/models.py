import jdatetime
from django.db import models


class ContactModel(models.Model):
    email = models.EmailField(verbose_name='ایمیل')
    phone = models.CharField(max_length=300, verbose_name='شماره تماس')
    title = models.CharField(max_length=300, verbose_name='عنوان')
    text = models.TextField(verbose_name='متن')
    sent_at = models.DateTimeField(auto_now_add=True, verbose_name='فرستاده شده در')

    def __str__(self):
        return self.email

    def get_date_fa(self):
        date_fa = jdatetime.GregorianToJalali(self.sent_at.year, self.sent_at.month, self.sent_at.day)
        final_date = date_fa.getJalaliList()
        return f'{final_date[0]}/{final_date[1]}/{final_date[2]}'

    class Meta:
        verbose_name = 'پیام'
        verbose_name_plural = 'پیام ها'
