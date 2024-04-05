from django.shortcuts import render,redirect 
from .models import game
 
def home(request):
    games = game.objects.all()
    return render(request,'home.html',{'game':games})
