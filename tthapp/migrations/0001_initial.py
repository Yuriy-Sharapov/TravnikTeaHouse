# Generated by Django 3.1.3 on 2020-12-06 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='clIngredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Ингредиент')),
                ('cost', models.CharField(max_length=200, verbose_name='Цена')),
                ('caloric', models.IntegerField(default=0, verbose_name='Калорийность')),
            ],
        ),
        migrations.CreateModel(
            name='clMenuCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Категория меню')),
            ],
        ),
        migrations.CreateModel(
            name='clUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Единица измерения')),
            ],
        ),
        migrations.CreateModel(
            name='clMenuPos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Пункт меню')),
                ('cost', models.CharField(max_length=200, verbose_name='Цена')),
                ('weight', models.IntegerField(default=0, verbose_name='Масса')),
                ('caloric', models.IntegerField(default=0, verbose_name='Калорийность')),
                ('img', models.CharField(max_length=200, verbose_name='Картинка')),
                ('menucategory', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tthapp.clmenucategory')),
            ],
        ),
        migrations.CreateModel(
            name='clIngrMenuPos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField(default=0, verbose_name='Масса')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tthapp.clingredient')),
                ('menupos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tthapp.clmenupos')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tthapp.clunit')),
            ],
        ),
    ]
