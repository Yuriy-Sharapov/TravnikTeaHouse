from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from tthapp.views import clMainView, clMenuView

from . import views

urlpatterns = [
    # пример /tthapp/
    path('', clMainView.as_view(), name='index'),
    # пример /tthapp/menucategory/5/
    path('menucategory/<int:category_id>/', clMenuView.as_view(), name='menucategory')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)