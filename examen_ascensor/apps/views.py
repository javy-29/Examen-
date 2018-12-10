from django.http import HttpResponse
import requests
from django.shortcuts import redirect
from django.shortcuts import render
from  . import models
from django.http import HttpResponse, HttpResponseRedirect
from .forms import OrdenForm,LoginForm
from .models import Tecnico
from .models import Orden
from .models import Cliente

usuarioLogeado = 0

# Create your views here.

def logout(request):
    global usuarioLogeado
    usuarioLogeado=0
    return redirect('login')

def index(request):
   
    global usuarioLogeado
    if usuarioLogeado == 0:
        return redirect('login')
    return render(request,'index.html',{'usuario': usuarioLogeado})
    
    
def login(request):
  
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            print("FORMA VALIDA")
            data=form.cleaned_data
            usuarioValidado = Tecnico.objects.all().filter(usuario=data.get("usuario"),contraseña=data.get("contraseña"))
            if usuarioValidado.count() == 1:
                global usuarioLogeado
                usuarioLogeado = usuarioValidado.first()
                return redirect('index')
    else:

        form = LoginForm()
    return render(request,'login.html', {'form': form})

def registrarorden(request):
    if usuarioLogeado == 0:
        return redirect('login')
    form = OrdenForm()
    if request.method == "POST":
        form = OrdenForm(request.POST)
        if form.is_valid():
            Orden = form.save(commit=False)
            Orden.save()
            return redirect('index')
    else:
        form = OrdenForm()
    return render(request, 'registrarorden.html', {'form': form, 'usuario': usuarioLogeado})


#agregar
def index(request):#deberia funcionar con o sin esto, debido a que ya hay un "def index"
	return render(request, 'index.html')