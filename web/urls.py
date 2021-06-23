from django.conf.urls import url
from . import views


app_name = 'femme'


urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^abc/$', views.abc, name="abc"),
    url(r'^cap/$', views.cap, name="cap"),
    url(r'^ar/$', views.ar, name="ar"),
    url(r'^cm/$', views.cm, name="cm"),
    url(r'^arc/$', views.arc, name="arc"),
    url(r'^anima/$', views.anima, name="anima"),
    url(r'^hom/$', views.hom, name="hom"),
    url(r'^comp/$', views.comp, name="comp"),
    url(r'^para/$', views.para, name="para"),
    url(r'^dent/$', views.dent, name="dent"),
    url(r'^avi/$', views.avi, name="avi"),
    url(r'^la/$', views.la, name="la"),
    url(r'^abt/$', views.abt, name="abt"),
    url(r'^agr/$', views.agr, name="agr"),
    url(r'^tm/$', views.tm, name="tm"),
    url(r'^des/$', views.des, name="des"),
    url(r'^pha/$', views.pha, name="pha"),
    url(r'^vet/$', views.vet, name="vet"),
    url(r'^cnt/$', views.cnt, name="cnt"),
    url(r'^rsc/$', views.rsc, name="rsc"),
    url(r'^ms/$', views.ms, name="ms"),










    

]
