from django.shortcuts import render,redirect
from Minformation.form import sig,sig1,sig2
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import PasswordResetView



# Create your views here.
def userform(request):
    if request.user.is_authenticated:
        return redirect('/nav')
    else:
        if request.method == 'POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            
            if password!=None:
                print('else body')
                user=authenticate(request,username=username,password=password)
                if user is not None:
                    login(request,user)
                    return redirect('/nav')
                else:
                    messages.error(request,'Username and Password is invalid')   

            elif password==None:
                form=sig(request.POST)
                print('post request')
                if form.is_valid():
                    print('valid form')
                    form.save()
                    return redirect('/nav')
                print('form error')  
        return render(request,'Minformation/userform.html')

def forget(request):
    a=request.POST.get('username')
    form=sig1(a,request.POST)
    x=request.POST.get('new_password1')
    if request.method=='POST':
        if User.objects.filter(username=a):
            form=sig1(a,request.POST)
            if form.is_valid():
                u=User.objects.get(username=a)
                u.set_password(x)
                u.save()
                return redirect('/form')
    return render (request,'Minformation/forgetpassword.html')


def logo(request):
    return redirect('/form')

def emailver(request):
    return render(request,'Minformation/email.html')

def mail_sent(request):
    return render(request,'Minformation/mail_sent.html')

def emailcon(request):
    return render(request,'Minformation/emailcon.html')

def form1(request):
    a=sig2()
    return render(request,'Minformation/aa.html',{'a':a})

def nav(request):
    return render(request,'Minformation/nav.html')


def marvelmovies(request):
    return render(request,'Minformation/marvelmovies.html')

def quotes(request):
    return render(request,'Minformation/quotes.html')


def movies(request):
    return render(request,'Minformation/movies.html')

def series(request):
    return render(request,'Minformation/series.html')

def phase1(request):
    return render(request,'Minformation/phase1.html')

def phase2(request):
    return render(request,'Minformation/phase2.html')

def phase3(request):
    return render(request,'Minformation/phase3.html')

def phase4(request):
    return render(request,'Minformation/phase4.html')

def phase5(request):
    return render(request,'Minformation/phase5.html')

def demo(request):
    return render(request,'Minformation/demo.html')

#Movie Details Section............................................................................................................
def WakandaForever(request):
    return render(request,'Movie_Detail/WakandaForever.html')

def Ant_Man_and_Wasp(request):
    return render(request,'Movie_Detail/Ant-Man_and_Wasp.html')

def Ant_Man_and_Wasp_Quantamania(request):
    return render(request,'Movie_Detail/Ant-Man_and_Wasp_Quantamania.html')

def Guardians_of_Galaxy2(request):
    return render(request,'Movie_Detail/Guardians_of_Galaxy2.html')

def Avengers_EndGame(request):
    return render(request,'Movie_Detail/AvengersEndGame.html')

def Shangchi(request):
    return render(request,'Movie_Detail/Shangchi.html')

def Avengers1(request):
    return render(request,'Movie_Detail/Avengers1.html')

def CaptainAmericaCivilWar(request):
    return render(request,'Movie_Detail/CaptainAmericaCivilWar.html')

def DoctorStrange1(request):
    return render(request,'Movie_Detail/DoctorStrange1.html')

def Hulk1(request):
    return render(request,'Movie_Detail/Hulk1.html')

def IronMan1(request):
    return render(request,'Movie_Detail/IronMan1.html')

def ThorRagnorok(request):
    return render(request,'Movie_Detail/ThorRagnorok.html')

def CaptainAmerica1(request):
    return render(request,'Movie_Detail/CaptainAmerica1.html')

def AntMan1(request):
    return render(request,'Movie_Detail/AntMan1.html')

def GuardiansOfGalaxy1(request):
    return render(request,'Movie_Detail/GuardiansOfGalaxy1.html')

def IronMan3(request):
    return render(request,'Movie_Detail/IronMan3.html')

def CaptainAmerica2(request):
    return render(request,'Movie_Detail/CaptainAmerica2.html')

def Thor2(request):
    return render(request,'Movie_Detail/Thor2.html')

def AvengersAgeOfUltron(request):
    return render(request,'Movie_Detail/AvengersAgeOfUltron.html')

def Thor1(request):
    return render(request,'Movie_Detail/Thor1.html')

def IronMan2(request):
    return render(request,'Movie_Detail/IronMan2.html')

def AvengersInfinityWar(request):
    return render(request,'Movie_Detail/AvengersInfinityWar.html')

def BlackPanther1(request):
    return render(request,'Movie_Detail/BlackPanther1.html')

def DoctorStrange2(request):
    return render(request,'Movie_Detail/DoctorStrange2.html')

def Thor4(request):
    return render(request,'Movie_Detail/Thor4.html')

def SpidermanHomecoming(request):
    return render(request,'Movie_Detail/SpidermanHomecoming.html')

def SpidermanNoWayHome(request):
    return render(request,'Movie_Detail/SpidermanNoWayHome.html')

def SpidermanFarFromHome(request):
    return render(request,'Movie_Detail/SpidermanFarFromHome.html')

def BlackWidow1(request):
    return render(request,'Movie_Detail/BlackWidow1.html')

def CaptainMarvel1(request):
    return render(request,'Movie_Detail/CaptainMarvel1.html')

def GuardiansOfGalaxy3(request):
    return render(request,'Movie_Detail/GuardiansOfGalaxy3.html')

def Spiderman1(request):
    return render(request,'Movie_Detail/Spiderman1.html')

def Spiderman2(request):
    return render(request,'Movie_Detail/Spiderman2.html')

def Spiderman3(request):
    return render(request,'Movie_Detail/Spiderman3.html')

def TheAmazing1(request):
    return render(request,'Movie_Detail/TheAmazing1.html')

def TheAmazing2(request):
    return render(request,'Movie_Detail/TheAmazing2.html')

def Venom1(request):
    return render(request,'Movie_Detail/Venom1.html')

def Venom2(request):
    return render(request,'Movie_Detail/Venom2.html')

def Deadpool1(request):
    return render(request,'Movie_Detail/Deadpool1.html')

def Deadpool2(request):
    return render(request,'Movie_Detail/Deadpool2.html')

#Series...........................................................................
def MoonKnight(request):
    return render(request,'Series/MoonKnight.html')

def Groot1(request):
    return render(request,'Series/Groot1.html')

def Loki1(request):
    return render(request,'Series/Loki1.html')

def HolidaySpecial(request):
    return render(request,'Series/HolidaySpecial.html')

def FalconWinter(request):
    return render(request,'Series/FalconWinter.html')

def WhatIf(request):
    return render(request,'Series/WhatIf.html')

def WandaVision(request):
    return render(request,'Series/WandaVision.html')

def Hawkye(request):
    return render(request,'Series/Hawkye.html')

def SheHulk(request):
    return render(request,'Series/SheHulk.html')

#email-Verification....................................................................................





