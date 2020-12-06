from django.shortcuts import render
from django.http import HttpResponse
#from tthapp.models import Student,Course,Mark
#from tthapp.forms import SearchForm,StudentForm
from django.db.models import Max
from django.views.generic import DetailView,ListView

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")