from django.shortcuts import render

def inicio(request):
    return render(request,'index.html',context={})

def lisar(request):
    return render(request, 'family.html',context={})

    