from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
import subprocess

def principal_view(request):

    subproceso = subprocess.Popen(
        ['/redNeuronal/ChatBot_Algorithm','python', 'chat.py'], 
        stdout=subprocess.PIPE,
        shell=True
    )
    salida, error = subproceso.communicate()
    print(salida)
    print("\n")
    print(type(salida))
    return render(request,'./principal.html')

