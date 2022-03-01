from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, HttpResponse, redirect
from accounts.models import CreateUserForm
from myapp.models import KycDetails,Wallet,Dash
from myapp.form import KycForm


def signup(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/index/explore')
    else:
        form = CreateUserForm()
        return render(request, 'signup.html', {'signup': form})


def signin(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/index/explore')
    else:
        form = AuthenticationForm()
    return render(request, 'signin.html', {'signin': form})


def signout(request):
    logout(request)
    return redirect('/')


def kyc(request):
    if request.method == "POST":
        k = KycDetails()
        k.FirstName = request.POST.get('fname')
        k.LastName = request.POST.get('lname')
        k.Bod = request.POST.get('bod')
        k.PhNumber = request.POST.get('mnumber')
        if request.POST.get('gen') == 'Male':
            k.Gender = 'M'
        else:
            k.Gender = 'F'
        if request.POST.get('mat') == 'Single':
            k.Marital = 'S'
        else:
            k.Marital = 'M'
        k.Pan = request.POST.get('pnumber')
        k.AadharNumber = request.POST.get('anumber')
        k.AadharPhoto = request.POST.get('apic')
        k.PanPhoto = request.POST.get('ppic')
        k.UserPhoto = request.POST.get('upic')
        k.Signature = request.POST.get('spic')
        k.user = request.user
        k.save()
        return redirect('/index/explore')

    return render(request, 'kyc.html')
