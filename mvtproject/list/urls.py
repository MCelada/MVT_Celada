from django.urls import path

from list.views import list_family, create_family

urlpatterns = [

    path('list_family/',list_family,name='list_family'),
    path('create_family/', create_family),

]