"""
URL configuration for minfo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from Minformation import views
from django.contrib.auth import views as v



urlpatterns = [
    path('admin/', admin.site.urls),
    path('form/',views.userform,name='form'),
    path('verification',views.emailver),
    path('forget/',views.forget),
    path('nav/',views.nav,name='nav'),
    path('marvelmovies/',views.marvelmovies,name='marvelmovies'),
    path('series/',views.series),
    path('phase/',views.quotes),
    path('movies/',views.movies),
    path('phase1/',views.phase1),
    path('phase2/',views.phase2),
    path('phase3/',views.phase3),
    path('phase4/',views.phase4),
    path('phase5/',views.phase5),
    path('demo',views.demo),
    path('sig',views.form1,name='form1'),
    #movie details Section..................................................
    path('WakandaForever/',views.WakandaForever),
    path('Antman_and_Wasp/',views.Ant_Man_and_Wasp),
    path('Antman_and_Wasp_Quantamania/',views.Ant_Man_and_Wasp_Quantamania),
    path('Guardians_of_Galaxy2/',views.Guardians_of_Galaxy2),
    path('AvengersEndGame/',views.Avengers_EndGame),
    path('Shangchi/',views.Shangchi),
    path('Avengers1/',views.Avengers1),
    path('CaptainAmericaCivilWar/',views.CaptainAmericaCivilWar),
    path('DoctorStrange1/',views.DoctorStrange1),
    path('Hulk1/',views.Hulk1),
    path('IronMan1/',views.IronMan1),
    path('ThorRagnorok/',views.ThorRagnorok),
    path('CaptainAmerica1/',views.CaptainAmerica1),
    path('AntMan1/',views.AntMan1),
    path('GuardiansOfGalaxy1/',views.GuardiansOfGalaxy1),
    path('IronMan3/',views.IronMan3),
    path('CaptainAmerica2/',views.CaptainAmerica2),
    path('Thor2/',views.Thor2),
    path('AvengersAgeOfUltron/',views.AvengersAgeOfUltron),
    path('Thor1/',views.Thor1),
    path('IronMan2/',views.IronMan2),
    path('AvengersInfinityWar/',views.AvengersInfinityWar),
    path('BlackPanther1/',views.BlackPanther1),
    path('DoctorStrange2/',views.DoctorStrange2),
    path('Thor4/',views.Thor4),
    path('SpidermanHomecoming/',views.SpidermanHomecoming),
    path('SpidermanNoWayHome/',views.SpidermanNoWayHome),
    path('SpidermanFarFromHome/',views.SpidermanFarFromHome),
    path('BlackWidow1/',views.BlackWidow1),
    path('CaptainMarvel1/',views.CaptainMarvel1),
    path('GuardiansOfGalaxy3/',views.GuardiansOfGalaxy3),
    #Marvel Legacy Movies.....................................................................................
    path('Deadpool1/',views.Deadpool1),
    path('Deadpool2/',views.Deadpool2),

    #Spiderverse..............................................................................................
    path('Spiderman1/',views.Spiderman1),
    path('Spiderman2/',views.Spiderman2),
    path('Spiderman3/',views.Spiderman3),
    path('TheAmazing1/',views.TheAmazing1),
    path('TheAmazing2/',views.TheAmazing2),
    path('Venom1/',views.Venom1),
    path('Venom2/',views.Venom2),
    #Series...................................................................................................
    path('MoonKnight/',views.MoonKnight),
    path('Groot1/',views.Groot1),
    path('Loki1/',views.Loki1),
    path('FalconWinter/',views.FalconWinter),
    path('WhatIf/',views.WhatIf),
    path('WandaVision/',views.WandaVision),
    path('Hawkye/',views.Hawkye),
    path('HolidaySpecial/',views.HolidaySpecial),
    path('SheHulk/',views.SheHulk),

    #......logout....................................
    path('accounts/',include('django.contrib.auth.urls')),
    path('logout/',views.logo),
    #Forget Password........................................
    path('reset_password/',v.PasswordResetView.as_view(template_name='Minformation/email.html')),
    path('reset_password_sent/',v.PasswordResetDoneView.as_view(template_name='Minformation/mail_sent.html')),
    path('reset/<uidb64>/<token>/',v.PasswordResetConfirmView.as_view(template_name='Minformation/forgetpassword.html'),name='password_reset_confirm'),
    path('reset_password_complete/',v.PasswordResetCompleteView.as_view(template_name='Minformation/emailcon.html'),name='password_reset_complete'),
    
    
path('mail_sent/',views.mail_sent)


    
    


]
'''
'


'''