# Generated by Django 3.1.3 on 2020-12-06 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tthapp', '0005_auto_20201206_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clmenupos',
            name='img',
            field=models.ImageField(blank=True, height_field=200, max_length=200, upload_to='../static/image', verbose_name='Картинка', width_field=200),
        ),
    ]
