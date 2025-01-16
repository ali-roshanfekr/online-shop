# Generated by Django 5.1.3 on 2024-12-21 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_setting_module', '0002_alter_logomodel_image_alter_slidermodel_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='logomodel',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='slidermodel',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
