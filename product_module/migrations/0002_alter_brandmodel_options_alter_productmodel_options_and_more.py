# Generated by Django 5.1.3 on 2024-11-24 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brandmodel',
            options={'verbose_name': 'دسته بندی', 'verbose_name_plural': 'دسته بندی ها'},
        ),
        migrations.AlterModelOptions(
            name='productmodel',
            options={'verbose_name': 'محصول', 'verbose_name_plural': 'محصولات'},
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='descript',
            field=models.TextField(),
        ),
    ]
