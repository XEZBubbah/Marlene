from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
import subprocess
from redNeuronal.ChatBot_Algorithm.chat import main
from multiprocessing import Process
from background_task import background


@background(schedule=5)
def secondTask():
    print("Ejecutando main xDDDD")
    main()
    print("Ejecutando main xDDDD")
    

def principal_view(request):
    secondTask()
    return render(request,'./principal.html')

