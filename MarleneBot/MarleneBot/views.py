from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
import subprocess
from redNeuronal.ChatBot_Algorithm import chat
from multiprocessing import Process

def principal_view(request):
    
    proceso1 = Process(target=chat)

    return render(request,'./principal.html')

