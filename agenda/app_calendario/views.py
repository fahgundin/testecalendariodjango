from django.shortcuts import render
from datetime import date
from calendar import HTMLCalendar
from .models import Registros


def home(request):
    data_atual = date.today()
    
    cal = HTMLCalendar().formatmonth(data_atual.year, data_atual.month)
    
    
    return render(request,'home.html',{
        "year" : data_atual.year,
        "month" : data_atual.month,
        "cal" : cal,
        "registros" : Registros.objects.filter(data__year=data_atual.year, data__month=data_atual.month).all
    })

def calendario(request, ano, mes):
    cal = HTMLCalendar().formatmonth(ano, mes)
    
    
   
    
    
    
    return render(request,'home.html',{
        "ano" : ano,
        "mes" : mes,
        "cal" : cal,
        "registros" : Registros.objects.filter(data__year = ano ,data__month= mes ).values()
        
    })

def registros(request):
    novo_registro = Registros()
    novo_registro.data = request.POST.get('data')
    novo_registro.oqfoifeito = request.POST.get('oqfoifeito')
    print(novo_registro.data)
    print(novo_registro.oqfoifeito)
    novo_registro.save()
    
    
    
    
    
    return render(request,'registro.html')
