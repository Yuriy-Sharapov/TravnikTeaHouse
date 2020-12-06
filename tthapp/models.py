import datetime

from django.db import models
from django.utils import timezone
from django.core.files.storage import FileSystemStorage

### Категория меню
class clMenuCategory(models.Model):
    name         = models.CharField(verbose_name="Категория меню",max_length=200)

    # Отображение названия объекта
    def __str__(self):
      return self.name

fs = FileSystemStorage(location='/static/image')

### Позиция меню
class clMenuPos(models.Model):
    menucategory = models.ForeignKey(clMenuCategory, on_delete=models.PROTECT)
    name         = models.CharField(verbose_name="Пункт меню", max_length=200)
    descr        = models.CharField(verbose_name="Описание", max_length=200, blank=True)
    cost         = models.IntegerField(verbose_name="Цена",default=0)
    weight       = models.IntegerField(verbose_name="Масса",default=0)
    caloric      = models.IntegerField(verbose_name="Калорийность",default=0)
    img          = models.ImageField(verbose_name="Картинка",upload_to=fs, blank=True)
    #img          = models.ImageField(verbose_name="Картинка",upload_to="../static/image", height_field=200, width_field=200, max_length=200, blank=True)

    # Отображение названия объекта
    def __str__(self):
      return self.name

### Ингредиент
class clIngredient(models.Model):
    name         = models.CharField(verbose_name="Ингредиент", max_length=200)
    cost         = models.IntegerField(verbose_name="Цена закупки",default=0)
    caloric      = models.IntegerField(verbose_name="Калорийность",default=0)

    # Отображение названия объекта
    def __str__(self):
      return self.name

### Единица измерения
class clUnit(models.Model):
    name         = models.CharField(verbose_name="Единица измерения",max_length=200)

    # Отображение названия объекта
    def __str__(self):
      return self.name

### Ингредиент в позиции меню
class clIngrMenuPos(models.Model):
    menupos      = models.ForeignKey(clMenuPos, on_delete=models.CASCADE)
    ingredient   = models.ForeignKey(clIngredient, on_delete=models.CASCADE)
    unit         = models.ForeignKey(clUnit, on_delete=models.PROTECT)
    weight       = models.IntegerField(verbose_name="Масса",default=0)

    # Отображение названия объекта
    def __str__(self):
      return self.menupos.name + ": " + self.ingredient.name + " " + str(self.weight) + ", " + self.unit.name