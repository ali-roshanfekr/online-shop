from django.db import models

from user_module.models import User

class CategoryModel(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    slug = models.SlugField(max_length=300, null=True, db_index=True, blank=True, verbose_name='عنوان در شبکه')

    def save(self, *args, **kwargs):
        self.slug = self.title.replace(' ', '-')
        return super(CategoryModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class BrandModel(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    slug = models.SlugField(max_length=300, null=True, db_index=True, blank=True, verbose_name='عنوان در شبکه')

    def save(self, *args, **kwargs):
        self.slug = self.title.replace(' ', '-')
        return super(BrandModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'برند'
        verbose_name_plural = 'برند ها'


class ProductModel(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    price = models.IntegerField(verbose_name='قیمت')
    descript = models.TextField(verbose_name='توضیحات')
    is_active = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')
    slug = models.SlugField(max_length=300, null=True, db_index=True, blank=True, verbose_name='عنوان در شبکه')
    brand = models.ManyToManyField(BrandModel, verbose_name='برند')
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, null=True, verbose_name='دسته بندی')
    image = models.ImageField(upload_to='uploads/product_img/', null=True, verbose_name='تصویر')
    number = models.IntegerField(default=0, verbose_name='تعداد')

    def save(self, *args, **kwargs):
        self.slug = self.title.replace(' ', '-')
        return super(ProductModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'
