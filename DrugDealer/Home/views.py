from django.shortcuts import render
from django.http import HttpResponse

#render for the home page
def home(request):
    return render(request, 'DrugDealerHomePage.html')

#render for the about page
def about(request):
    return render(request, 'DrugDealerAboutPage.html')

#render for the rules page
def rules(request):
    return render(request, 'DrugDealerRulePage.html')

#render for a game
def lobby(request,gameroom_code):
	return HttpResponse("your lobby code %s" % gameroom_code)

#render for a game
def game(request,gameroom_code):
	return HttpResponse("your game code %s" % gameroom_code)
