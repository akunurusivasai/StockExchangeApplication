import time
import requests
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from requests import Response
from . import form
from myapp.models import Ticket, Dash, Wallet, KycDetails, Watchlist
import yfinance as yf
from bs4 import BeautifulSoup
from get_all_tickers import get_tickers as gt
from . import api as api
from .form import Dashboard

l = []


@login_required(login_url="/accounts/signin")
def explore(request):
    # stock()

    return render(request, "explore.html", {'stocks': l})


def fetch(request, name, sym):
    if request.method == "POST":
        if name == 'buy':
            shares = int(request.POST.get('count'))
            price = float(request.POST.get('price'))
            try:
                b = Dash.objects.get(stocks=sym, user=request.user)
                w = Wallet.objects.get(user=request.user)
                b.count = b.count + shares
                b.price = price
                w.amount = w.amount - price * shares
                w.save()
                b.save()
            except:
                b = Dash()
                b.user = request.user
                b.stocks = sym
                b.count = shares
                b.price = price
                b.save()
        else:
            w = Wallet.objects.get(user=request.user)
            shares = int(request.POST.get('sellcount'))
            price = float(request.POST.get('sellprice'))
            try:
                s = Dash.objects.get(stocks=sym, user=request.user)
                print('done')
                print('else')
                if s.count == shares:
                    print('if')
                    s.delete()
                    w.amount = w.amount + price * shares
                    w.save()
                elif s.count > shares:
                    print(">")
                    s.count = s.count - shares
                    s.save()
                    w.amount = w.amount + price * shares
                    w.save()
                elif s.count < shares:
                    print("<")
                    print('insuffient shares')
                else:
                    print('you dont have this stock')
            except:
                print('else excption')

        return redirect('/index/dashboard')
    return render(request, 'login.html')


def wallet(request):
    try:
        w = Wallet.objects.get(user=request.user)
    except:
        w = Wallet()
        w.amount = 0
        w.user = request.user
        w.name = request.user.username
        w.save()
    if request.method == 'POST':
        if request.POST.get('with') is None:
            w.amount = w.amount + int(request.POST.get('add'))
            w.save()
            return redirect('/index/wallet')
        else:
            w.amount = w.amount - int(request.POST.get('with'))
            w.save()
            return redirect('/index/wallet')
    return render(request, 'wallet.html', {'w': w})


def dashboard(request):
    d = Dash.objects.filter(user=request.user)
    li = []
    for i in d:
        if i.count > 0:
            cp, c = getprice(i.stocks)
            li.append(Board(i.stocks, i.count, i.price, cp, i.count * cp, round(i.count * cp - i.count * i.price,2),i.date))
    return render(request, 'dashboard.html', {'d': li})


def plot(request, name):
    price1, label1 = api.finance(name, '1d')
    price2, label2 = api.finance(name, '5d')
    price3, label3 = api.finance(name, '1mo')
    price4, label4 = api.finance(name, '6mo')
    price5, label5 = api.finance(name, '1y')
    price6, label6 = api.finance(name, '5y')
    price7, label7 = api.finance(name, 'max')
    s = api.details(name)
    try:
        u = KycDetails.objects.get(user=request.user)
        user = True
    except:
        user = False
    try:
        w = Wallet.objects.get(user=request.user)
    except:
        w = Wallet()
        w.user = request.user
        w.save()
    try:
        d = Dash.objects.get(stocks=name, user=request.user)
        d = d.count
    except:
        d = 0
    return render(request, 'plot.html', {'price1': price1, 'index1': label1, 'price2': price1, 'index2': label2,
                                         'price3': price3, 'index3': label3, 'price4': price4, 'index4': label4,
                                         'price5': price5, 'index5': label5, 'price6': price6, 'index6': label6,
                                         'price7': price7, 'index7': label7, 's': s, 'u': user, 'w': w, 'd': d})


def getprice(i):
    url = 'https://in.finance.yahoo.com/quote/' + i
    r = requests.get(url)
    web = BeautifulSoup(r.text, 'html.parser')
    try:
        profit = web.find('span', {"class": 'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)'}).text
    except:
        profit = '0.0 (0.00)'

    try:
        prices = web.find('span', {"class": 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text
    except:
        prices = '0.00'

    prices = prices.split(',')
    price = ''
    for i in prices:
        price = price + i

    return float(price), profit


def info(i):
    ioc = yf.Ticker(i)
    st = ioc.info
    for key, value in st.items():
        print(key, ':', value)


def insert():
    details = ['IBM', 'QRTEA', 'TSLA', 'AAPL', 'SONY', 'TTM', 'TCS', 'FB', 'WIT', 'CTSH', 'F', 'UBER', 'INTC', 'MSFT']
    for i in range(0, 14):
        s = yf.Ticker(details[i])
        name = s.info['shortName']
        logo = s.info['logo_url']
        t = Ticket(name=details[i], shortname=name, img=logo)
        t.save()
        print(t.shortname, t.name)
        print(t.img)


class Details:
    def __init__(self, name, shortname, logo, price, change):
        self.name = name
        self.shortname = shortname
        self.logo = logo
        self.price = price
        self.change = change

    def __str__(self):
        return self.name


def stock():
    stocks = Ticket.objects.all().order_by('name')
    for i in stocks:
        price, change = getprice(i.name)
        l.append(Details(name=i.name, shortname=i.shortname, logo=i.img, price=price, change=change))


class Board:
    def __init__(self, name, shares, price, cp, cv, profit,date):
        self.name = name
        self.shares = shares
        self.price = price
        self.cp = cp
        self.cv = cv
        self.profit = profit
        self.date=date


def watchlist(request, name):
    if name == 'list':
        w=[]
        try:
            wl = Watchlist.objects.get(user=request.user)
        except:
            wl = Watchlist()
            wl.user = request.user
            wl.save()
        return render(request, 'watchlist.html', {'wl': wl})
    else:
        wl = Watchlist()
        wl.user = request.user
        wl.symbol = name
        wl.save()
        return HttpResponse('ok')


class Watch:
    def __init__(self, sym, price):
        self.sym = sym
        self.price = price


stock()
