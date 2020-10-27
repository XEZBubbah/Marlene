from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template


def principal_view(request):

    return render(request,'./principal.html')

