from ast import Return
import email
from multiprocessing import context
from django.shortcuts import render
from accounts.models import Account

# Create your views here.

def registrarse(request):
    context={}

    if request.method == 'POST':
        rol=request.POST['rol']
        password= request.POST['password']
        confirmPassword= request.POST['confirmPassword']
        username=request.POST['username']
        email=request.POST['correo']

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

    return render(request, 'registro.html',context)