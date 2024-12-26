# Generated by Django 5.1.3 on 2024-11-25 18:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0002_alter_brandmodel_options_alter_productmodel_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, max_length=300, null=True)),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
            },
        ),
        migrations.AlterModelOptions(
            name='brandmodel',
            options={'verbose_name': 'برند', 'verbose_name_plural': 'برند ها'},
        ),
        migrations.AddField(
            model_name='productmodel',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product_module.categorymodel'),
        ),
    ]