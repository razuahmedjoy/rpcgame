from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import player
import random

def home(request):
    return render(request,'home.html')

def play(request):
    if request.method == 'POST':
        playername = request.POST['playername']

        p = player(name=playername)
        p.save()

        return render(request,'play.html')

    return redirect('home')

def num_to_string(r):
    c = ""
    if r == 1:
        c = "Rock"
    elif r == 2:
        c = "Paper"
    elif r == 3:
        c = "Sizor"
    return c
def num_to_stringfortag(r):
    c = ""
    if r == 1:
        c = "hand-rock"
    elif r == 2:
        c = "sticky-note"
    elif r == 3:
        c = "cut"
    return c


def calculate(request):
    if request.method == 'POST':
        uchoice = request.POST['uchoice']
        uchoice = int(uchoice)

        userc = num_to_string(uchoice)
        userctag = num_to_stringfortag(uchoice)
        print(type(uchoice))

        comp = random.randint(1, 3)
        comchoice = num_to_stringfortag(comp)
        comchoicetext = num_to_string(comp)

        res = uchoice - comp
        if res == 0:
            win = 3
        elif res > 0:
            if res == 1:
                win = 1
                # userpt += 1
                # print(f"Your Point {userpt}\n")
            else:
                win = 0
                # compt += 1
                # print(f"Computer Point {compt}\n")
        else:
            if res == -1:
                win = 0
                # compt += 1
                # print(f"Computer Point {compt}\n")
            else:
                win = 1
                # userpt += 1
                # print(f"Your Point {userpt}\n")


        context = {
            'userc': userc,
            'userctag':userctag,
            'comchoice':comchoice,
            'win' : win,
            'comchoicetext':comchoicetext,
        }
        return render(request,'play.html',context)
    return redirect('home')