from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import bcrypt
from models import *

def index(request):
    return render(request, 'amazon/index.html')

def buy(request):
    if request.POST['id'] == '001':
        price = 19.99
    if request.POST['id'] == '002':
        price = 29.99
    if request.POST['id'] == '003':
        price = 4.99
    if request.POST['id'] == '004':
        price = 49.99
    request.session['price'] = price * int(request.POST['quantity'])
    request.session['quantity'] = int(request.POST['quantity']) + int(request.session['quantity'])
    request.session['total'] = request.session['price'] + request.session['total']
    return redirect('/reciept')

def reciept(request):
    return render(request, 'amazon/reciept.html')