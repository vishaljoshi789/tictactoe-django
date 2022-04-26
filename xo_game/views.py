from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Game

# Create your views here.


def home(request):
    return render(request, 'xo_game/home.html')


def join(request):
    if request.method == 'POST':
        gameid = request.POST['gameid']
        uname = request.POST['name']
        Game.objects.all()
        if Game.objects.filter(gameid=gameid):
            pass
        else:
            Game.objects.create(
                gameid=gameid
            )
        url = f'/game/{gameid}/{uname}'
        return redirect(url)
    return render(request, 'xo_game/join.html')


def game(request, **kwargs):
    return render(request, 'xo_game/game.html', {'gameid': kwargs['gameid'], 'player': kwargs['player']})
