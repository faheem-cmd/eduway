from django.contrib import admin

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



class engiAdmin(admin.ModelAdmin):
    list_display = ('title','content','contents','image')
admin.site.register(engi,engiAdmin)

class medAdmin(admin.ModelAdmin):
    list_display = ('titles','content','contents','image')

admin.site.register(med,medAdmin)


class artsAdmin(admin.ModelAdmin):
    list_display = ('title','content','contents','image')

admin.site.register(arts,artsAdmin)


class commAdmin(admin.ModelAdmin):
    list_display = ('title','content','contents','phone','image')

admin.site.register(comm,commAdmin)


class archAdmin(admin.ModelAdmin):
    list_display = ('title','content','contents','phone','image')

admin.site.register(arch,archAdmin)


class hmAdmin(admin.ModelAdmin):
    list_display = ('title','content','contents','phone','image')

admin.site.register(hm,hmAdmin)


class animationAdmin(admin.ModelAdmin):
    list_display = ('title','courses','website','phone','image')

admin.site.register(animation,animationAdmin)


class computerAdmin(admin.ModelAdmin):
    list_display = ('title','content','contents','phone','image')

admin.site.register(computer,computerAdmin)


class paramedAdmin(admin.ModelAdmin):
    list_display = ('title','content','contents','phone','image')

admin.site.register(paramed,paramedAdmin)


class dentalAdmin(admin.ModelAdmin):
    list_display = ('title','content','contents','phone','image')

admin.site.register(dental,dentalAdmin)


class aviationAdmin(admin.ModelAdmin):
    list_display = ('title','content','contents','phone','image')

admin.site.register(aviation,aviationAdmin)


class lawAdmin(admin.ModelAdmin):
    list_display = ('title','content','contents','phone','image')

admin.site.register(law,lawAdmin)


class aboutAdmin(admin.ModelAdmin):
    display = ('title')

admin.site.register(about,aboutAdmin)


class teamAdmin(admin.ModelAdmin):
    list_display = ('name','position','description','image')

admin.site.register(team,teamAdmin)


class designsAdmin(admin.ModelAdmin):
    list_display = ('title','content','contents','phone','image')

admin.site.register(designs,designsAdmin)



class pharmaAdmin(admin.ModelAdmin):
    list_display = ('title','content','contents','phone','image')

admin.site.register(pharma,pharmaAdmin)


class vetiAdmin(admin.ModelAdmin):
    list_display = ('title','content','contents','phone','image')

admin.site.register(veti,vetiAdmin)


class contactAdmin(admin.ModelAdmin):
        display = ('title')

admin.site.register(contact,contactAdmin)


class resourceAdmin(admin.ModelAdmin):
    list_display = ('title','content','website')

admin.site.register(resource,resourceAdmin)



class agriAdmin(admin.ModelAdmin):
    list_display = ('title','content','contents','phone','image')

admin.site.register(agri,agriAdmin)



class massAdmin(admin.ModelAdmin):
    list_display = ('title','content','contents','phone','image')

admin.site.register(mass,massAdmin)





