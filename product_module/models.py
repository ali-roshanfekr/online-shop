from django.db import models

# Create your models here.

class CategoryModel(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=300, null=True, db_index=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = self.title.replace(' ', '-')
        return super(CategoryModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

class BrandModel(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=300, null=True, db_index=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = self.title.replace(' ', '-')
        return super(BrandModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'برند'
        verbose_name_plural = 'برند ها'

class ProductModel(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    descript = models.TextField()
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(max_length=300, null=True, db_index=True, blank=True)
    brand = models.ManyToManyField(BrandModel)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='uploads/product_img/', null=True)

    def save(self, *args, **kwargs):
        self.slug = self.title.replace(' ', '-')
        return super(ProductModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

