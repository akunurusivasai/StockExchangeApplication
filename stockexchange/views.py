from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, HttpResponse, redirect
from pandas.io.formats import style
import myapp.api as api
from django.http import JsonResponse
from myapp.models import KycDetails


def index(request):
    user = request.user
    k = KycDetails.objects.get(user=user)
    return render(request, 'index.html', {'user': user, 'k': k})


def helo(request):
    if request.method == 'GET':
        inter = request.GET.get('st', '')
        price, label = api.getinterval(inter)
        return render(request, 'register.html', {'price': price, 'index': label})
    else:
        return HttpResponse('failed')


class plot:
    def __init__(self, interval, price, index):
        self.price = price
        self.interval = interval
        self.index = index


def home(request):
    return render(request, 'login.html')


def support(reuest):
    return render(reuest, 'support.html')
