
import datetime
from django.http import HttpResponse
from django.shortcuts import render,redirect
from controles_gastos.form import TransaçaoForm
from controles_gastos.models import Transação





def home1 (request):
    data = {}
    data['transações'] = ['L1','L2','L3']
    data['now'] = datetime.datetime.now()
    return render(request , 'home1.html',data)

def listagem (request):
    data = {}
    data['transações'] = Transação.objects.all()
    return render(request ,'listagem.html',data )

def nova_transação (request):
    data = {}
    form = TransaçaoForm(request.POST or None) 
    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    data['form'] = form  
    return render(request ,'form.html',data)

def update (request, pk):
    data = {}
    transaçao = Transação.objects.get(pk=pk)
    form = TransaçaoForm(request.POST or None, instance=transaçao)
    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    data['form']=form 
    data['transaçao'] = transaçao 
    return render(request ,'form.html', data)

def delete (request, pk):
    transaçao = Transação.objects.get(pk=pk)
    transaçao.delete()
    return redirect('url_listagem')
    
