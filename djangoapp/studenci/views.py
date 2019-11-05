from django.shortcuts import render
from django.http import HttpResponse
from studenci.models import Miasto, Uczelnia
from django.contrib import messages
from studenci.form import StudentLoginForm
from studenci.form import UczelniaForm


def index(request):
    return HttpResponse("Witaj w aplikacji Studenci!")
    # return render(request, 'pizza/index.html')


def news(request):
    return HttpResponse("<h1>Nowości u studentów</h1>")
    # return render(request, 'pizza/news.html')

def miasta(request):

    if request.method == 'POST':
        nazwa= request.POST.get('nazwa')
        kod= request.POST.get('kod')
        if len(nazwa.strip()):
            m = Miasto(nazwa=nazwa, kod=kod)
            m.save()
            messages.success(request, "Dane zapisano!")
        else:
            messages.error(request, "Błędne dane deb***!")

    miasta = Miasto.objects.all()
    kontekst = {
        'miasta': miasta
    }
    return render(request, 'studenci/miasta.html', kontekst)


def uczelnia(request):

    if request.method == 'POST':
        nazwa= request.POST.get('nazwa')
        if len(nazwa.strip()):
            u = Uczelnia(nazwa=nazwa)
            u.save()
            messages.error(request, "Dane zapisano!")
        else:
            messages.error(request, "Błędne dane deb***!")

    uczelnia = Uczelnia.objects.all()
    kontekst = {
        'uczelnia': uczelnia
    }
    return render(request, 'studenci/uczelnia.html', kontekst)

def login(request):

    if request.method == 'POST':
        nazwa= request.POST.get('nazwa')
        kod= request.POST.get('kod')
        if len(nazwa.strip()):
            m = Miasto(nazwa=nazwa, kod=kod)
            m.save()
            messages.success(request, "Dane zapisano!")
        else:
            messages.error(request, "Błędne dane!")
    else:
        form = StudentLoginForm()


    kontekst = { 'form': form }
    return render(request, 'studenci/login.html', kontekst)

def login2(request):

    if request.method == 'POST':
        nazwa= request.POST.get('nazwa')
        kod= request.POST.get('kod')
        if len(nazwa.strip()):
            m = Miasto(nazwa=nazwa, kod=kod)
            m.save()
            messages.success(request, "Dane zapisano!")
        else:
            messages.error(request, "Błędne dane!")
    else:
        form = UczelniaForm()


    kontekst = { 'form': form }
    return render(request, 'studenci/login2.html', kontekst)
