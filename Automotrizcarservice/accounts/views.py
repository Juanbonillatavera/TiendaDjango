from ast import Return
from contextlib import redirect_stderr
import email
from multiprocessing import context
from django.shortcuts import render,redirect
from accounts.models import Account
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.

def registrarse(request):
    context={}

    if request.method == 'POST':
        rol=request.POST['rol']
        password= request.POST['password']
        confirmPassword= request.POST['confirmPassword']
        username=request.POST['username']
        email=request.POST['email']

    #validacion de campos

        ok=True
        if not email:
            context['alarma']='Ingrese el correo electronico'
            ok=False
        if not password or len(password)<5:
            context['alarma']='Ingrese una contraseña de 5 o mas caracteres'
            ok=False 
        if password !=confirmPassword:
            context['alarma']='La contraseña no coincide'
            ok=False   

        #todo ok
        if ok:
            existe=Account.objects.filter(email=email).exists()
            if not existe:
                user=Account.objects.create_user(first_name=username,last_name=username,
                username=username,email=email,password=password)
                user.save()
                context['mensaje']='Usuario guardado con exito'
            else:
                context['alarma']= '¡ El correo ya existe!'
        

    print('--------')
    print(context)
    return render(request, 'registro.html',context)


    #Control de ingreso de usuarios#

def login(request):


    if request.method == 'POST':
        email=request.POST['email']
        password= request.POST['password']
        user= auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request,user)
            return render (request, 'index.html')

        else:
            return render(request,'login.html',{'alarma': 'Correo o contraseña invalida'})

    else:
        return render(request,'login.html')



@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')







