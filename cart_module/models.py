import jdatetime

from django.db import models

from user_module.models import User
from product_module.models import ProductModel


class InvoiceProductModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.PROTECT, verbose_name='محصول')
    number = models.IntegerField(verbose_name='تعداد')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='ساخته شده در')

    def get_date_fa(self):
        date_fa = jdatetime.GregorianToJalali(self.create_at.year, self.create_at.month, self.create_at.day)
        final_date = date_fa.getJalaliList()
        return f'{final_date[0]}/{final_date[1]}/{final_date[2]}'

    def reduce(self):
        self.product.number -= 1
        self.product.save()

    class Meta:
        verbose_name = 'فاکتور محصولات'
        verbose_name_plural = 'فاکتور های محصولات'


class InvoiceModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='کاربر')
    products = models.ManyToManyField(InvoiceProductModel, verbose_name='محصولات')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='ساخته شده در')

    def get_date_fa(self):
        date_fa = jdatetime.GregorianToJalali(self.create_at.year, self.create_at.month, self.create_at.day)
        final_date = date_fa.getJalaliList()
        return f'{final_date[0]}/{final_date[1]}/{final_date[2]}'

    def total(self):
        total = 0
        for product in self.products.all():
            total += int(product.product.price)*int(product.number)

        return total

    class Meta:
        verbose_name = 'فاکتور کاربر'
        verbose_name_plural = 'فاکتور های کاربران'
