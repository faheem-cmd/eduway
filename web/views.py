from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from web.models import engi
from web.models import med
from web.models import arts
from web.models import comm
from web.models import arch
from web.models import hm
from web.models import animation
from web.models import computer
from web.models import paramed
from web.models import dental
from web.models import aviation
from web.models import law
from web.models import about
from web.models import agri
from web.models import team
from web.models import designs
from web.models import pharma
from web.models import veti
from web.models import contact
from web.models import resource
from web.models import mass


def index(request):
    engi_datas = engi.objects.all()
    context = {
        "engi_datas" : engi_datas
    }
    return render(request,'web/index.html',context)


def abc(request):
    engi_datas = engi.objects.all()
    context = {
        "engi_datas" : engi_datas
    }
    return render(request, 'web/engin.html',context)

def cap(request):
    med_datas = med.objects.all()
    context = {
        "med_datas" : med_datas
    }
    return render(request, 'web/med.html',context)

def ar(request):
    arts_datas = arts.objects.all()
    context = {
        "arts_datas" : arts_datas
    }
    return render(request, 'web/arts.html',context)    


def cm(request):
    comm_datas = comm.objects.all()
    context = {
        "comm_datas" : comm_datas
    }
    return render(request, 'web/comm.html',context)    


def arc(request):
    arch_datas = arch.objects.all()
    context = {
        "arch_datas" : arch_datas
    }
    return render(request, 'web/arc.html',context)    



def hom(request):
    hm_datas = hm.objects.all()
    context = {
        "hm_datas" : hm_datas
    }
    return render(request, 'web/hotel.html',context)    


def anima(request):
    animation_datas = animation.objects.all()
    context = {
        "animation_datas" : animation_datas
    }
    return render(request, 'web/anima.html',context)    


def comp(request):
    computer_datas = computer.objects.all()
    context = {
        "computer_datas" : computer_datas
    }
    return render(request, 'web/computer.html',context) 


def para(request):
    paramed_datas = paramed.objects.all()
    context = {
        "paramed_datas" : paramed_datas
    }
    return render(request, 'web/para.html',context) 


def dent(request):
    dental_datas = dental.objects.all()
    context = {
        "dental_datas" : dental_datas
    }
    return render(request, 'web/dent.html',context) 


def avi(request):
    aviation_datas = aviation.objects.all()
    context = {
        "aviation_datas" : aviation_datas
    }
    return render(request, 'web/avi.html',context) 




def la(request):
    law_datas = law.objects.all()
    context = {
        "law_datas" : law_datas
    }
    return render(request, 'web/law.html',context) 


def abt(request):
    about_datas = about.objects.all()
    context = {
        "about_datas" : about_datas
    }
    return render(request, 'web/about.html',context) 




def agr(request):
    agri_datas = agri.objects.all()
    context = {
        "agri_datas" : agri_datas
    }
    return render(request, 'web/agri.html',context) 


def tm(request):
    team_datas = team.objects.all()
    context = {
        "team_datas" : team_datas
    }
    return render(request, 'web/team.html',context) 



def des(request):
    designs_datas = designs.objects.all()
    context = {
        "designs_datas" : designs_datas
    }
    return render(request, 'web/design.html',context) 


def pha(request):
    pharma_datas = pharma.objects.all()
    context = {
        "pharma_datas" : pharma_datas
    }
    return render(request, 'web/pharma.html',context) 


def vet(request):
    veti_datas = veti.objects.all()
    context = {
        "veti_datas" : veti_datas
    }
    return render(request, 'web/vet.html',context) 


def cnt(request):
    contact_datas = contact.objects.all()
    context = {
        "contact_datas" : contact_datas
    }
    return render(request, 'web/contact.html',context) 


def rsc(request):
    resource_datas = resource.objects.all()
    context = {
        "resource_datas" : resource_datas
    }
    return render(request, 'web/res.html',context) 


    
def ms(request):
    mass_datas = mass.objects.all()
    context = {
        "mass_datas" : mass_datas
    }
    return render(request, 'web/mass.html',context) 

















