from django.shortcuts import render
from django.http import HttpResponse
from tthapp.models import clMenuCategory, clMenuPos, clIngredient, clUnit, clIngrMenuPos
#from tthapp.forms import SearchForm,StudentForm
from django.db.models import Max
from django.views.generic import DetailView,ListView

# Create your views here.
def index(request):
    return render(request,'index.html')

def menucategory(request, category_id):
    #c = clMenuCategory.objects.get(pk=category_id)
    #response = "Вы зашли в категорию %s."
    #return HttpResponse(response % c.name)
    return render(request,'menu.html')