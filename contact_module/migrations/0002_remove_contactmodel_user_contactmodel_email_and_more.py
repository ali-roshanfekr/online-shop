# Generated by Django 5.1.3 on 2024-12-30 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_module', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactmodel',
            name='user',
        ),
        migrations.AddField(
            model_name='contactmodel',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='ایمیل'),
        ),
        migrations.AddField(
            model_name='contactmodel',
            name='phone',
            field=models.CharField(max_length=300, null=True, verbose_name='شماره تماس'),
        ),
    ]
