from django.shortcuts import render
from django.http import HttpResponse

from list.models import Listar

# Create your views here.

def list_family(request):
    list = Listar.objects.all()
    context = {
        'list' : list,
    }
    return render(request, 'family.html',context=context)

def create_family(request):
    Listar.objects.create(name='Jose',last_name='Celada',relationship='Padre',number=1123456789,it_lives=True)
    Listar.objects.create(name='Marcela',last_name='Esteban',relationship='Madre',number=1198765432,it_lives=False)
    Listar.objects.create(name='Lucas',last_name='Celada',relationship='Hermano',number=1167892345,it_lives=True)
    return HttpResponse('Family created')