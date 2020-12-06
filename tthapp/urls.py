from django.urls import path

from . import views

urlpatterns = [
    # пример /tthapp/
    path('', views.index, name='index'),
    # пример /tthapp/menucategory/5/
    path('menucategory/<int:category_id>/', views.menucategory, name='menucategory')
]
#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)