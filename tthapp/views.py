from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.http import HttpResponse
from tthapp.models import clMenuCategory, clMenuPos, clIngredient, clUnit, clIngrMenuPos
#from tthapp.forms import SearchForm,StudentForm
from django.db.models import Max
from django.views.generic import DetailView,ListView
from django.template import loader
from django.views import View

# Используем CBV (вью на классах)
class clMainView(ListView):
    model = clMenuCategory
    context_object_name = 'menucategory_list'
    template_name = 'index.html'

class clMenuView(ListView):
    context_object_name = 'menupos_list'
    template_name       = 'menu.html'

    # Фильтрация списка позиций меню по категории
    def get_queryset(self):
        self.clMenuCategory = get_object_or_404(clMenuCategory, id=self.kwargs['category_id'])
        return clMenuPos.objects.filter(menucategory=self.clMenuCategory)