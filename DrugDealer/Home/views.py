from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'DrugDealerHomePage.html')

def about(request):
    return render(request, 'DrugDealerAboutPage.html')
