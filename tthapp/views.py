from django.shortcuts import get_list_or_404, render
from django.http import HttpResponse
from tthapp.models import clMenuCategory, clMenuPos, clIngredient, clUnit, clIngrMenuPos
#from tthapp.forms import SearchForm,StudentForm
from django.db.models import Max
from django.views.generic import DetailView,ListView
from django.template import loader

# Create your views here.
def index(request):
    menucategory_list = clMenuCategory.objects.all()
    context = {'menucategory_list' : menucategory_list }
    return render(request,'index.html',context)

def menucategory(request, category_id):
    # Получаем объект текущей категории
    c = clMenuCategory.objects.get(pk=category_id)
    # Получаем список позиций меню в текущй категории
    menupos_list = get_list_or_404(clMenuPos, menucategory=c)
    context = {'menupos_list' : menupos_list }
    return render(request,'menu.html',context)