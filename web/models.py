from django.db import models

class engi(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    contents = models.URLField(default="", editable=True)
    image = models.ImageField(upload_to="web/engi")
    



    class Meta:
        db_table = 'web_engi'
        verbose_name = "engi"
        verbose_name_plural = "engi"

    def __unicode__(self):
        return self.title

class med(models.Model):
    titles = models.CharField(max_length=128)
    content = models.TextField()
    contents = models.URLField(default="", editable=False)
    image = models.ImageField(upload_to="web/med")
  

    class Meta:
        db_table = 'web_med'
        verbose_name = "med"
        verbose_name_plural = "med"

    def __unicode__(self):
        return self.titles

        
class arts(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    contents = models.URLField(default="", editable=True)
    image = models.ImageField(upload_to="web/arts")
    
    
    class Meta:
        db_table = 'web_arts'
        verbose_name = "arts"
        verbose_name_plural = "arts"

    def __unicode__(self):
        return self.title

        
class comm(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    contents = models.URLField(default="", editable=True)
    phone = models.TextField()
    image = models.ImageField(upload_to="web/engi")
    



    class Meta:
        db_table = 'web_comm'
        verbose_name = "comm"
        verbose_name_plural = "comm"

    def __unicode__(self):
        return self.title


class arch(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    contents = models.URLField(default="", editable=True)
    phone = models.TextField()
    image = models.ImageField(upload_to="web/engi")
    



    class Meta:
        db_table = 'web_arch'
        verbose_name = "arch"
        verbose_name_plural = "arch"

    def __unicode__(self):
        return self.title


class hm(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    contents = models.URLField(default="", editable=True)
    phone = models.TextField()
    image = models.ImageField(upload_to="web/engi")
    



    class Meta:
        db_table = 'web_hm'
        verbose_name = "hm"
        verbose_name_plural = "hm"

    def __unicode__(self):
        return self.title


class animation(models.Model):
    title = models.CharField(max_length=128)
    courses = models.TextField()
    website = models.URLField(default="", editable=True)
    phone = models.TextField()
    image = models.ImageField(upload_to="web/engi")
    



    class Meta:
        db_table = 'web_animation'
        verbose_name = "animation"
        verbose_name_plural = "animation"

    def __unicode__(self):
        return self.title



class computer(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    contents = models.URLField(default="", editable=True)
    phone = models.TextField()
    image = models.ImageField(upload_to="web/engi")
    



    class Meta:
        db_table = 'web_computer'
        verbose_name = "computer"
        verbose_name_plural = "computer"

    def __unicode__(self):
        return self.title


class paramed(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    contents = models.URLField(default="", editable=True)
    phone = models.TextField()
    image = models.ImageField(upload_to="web/engi")
    



    class Meta:
        db_table = 'web_paramed'
        verbose_name = "paramed"
        verbose_name_plural = "paramed"

    def __unicode__(self):
        return self.title



class dental(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    contents = models.URLField(default="", editable=True)
    phone = models.TextField()
    image = models.ImageField(upload_to="web/engi")
    



    class Meta:
        db_table = 'web_dental'
        verbose_name = "dental"
        verbose_name_plural = "dental"

    def __unicode__(self):
        return self.title



class aviation(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    contents = models.URLField(default="", editable=True)
    phone = models.TextField()
    image = models.ImageField(upload_to="web/engi")
    



    class Meta:
        db_table = 'web_aviation'
        verbose_name = "aviation"
        verbose_name_plural = "aviation"

    def __unicode__(self):
        return self.title


class law(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    contents = models.URLField(default="", editable=True)
    phone = models.TextField()
    image = models.ImageField(upload_to="web/engi")
    



    class Meta:
        db_table = 'web_law'
        verbose_name = "law"
        verbose_name_plural = "law"

    def __unicode__(self):
        return self.title


class about(models.Model):
    title = models.CharField(max_length=128)


    class Meta:
        db_table = 'web_about'
        verbose_name = "about"
        verbose_name_plural = "about"

    def __unicode__(self):
        return self.title


class agri(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    contents = models.URLField(default="", editable=True)
    phone = models.TextField()
    image = models.ImageField(upload_to="web/engi")
    



    class Meta:
        db_table = 'web_agri'
        verbose_name = "agri"
        verbose_name_plural = "agri"

    def __unicode__(self):
        return self.title


class team(models.Model):
    name = models.CharField(max_length=128)
    position = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to="web/engi")
    



    class Meta:
        db_table = 'web_team'
        verbose_name = "team"
        verbose_name_plural = "team"

    def __unicode__(self):
        return self.name



class designs(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    contents = models.URLField(default="", editable=True)
    phone = models.TextField()
    image = models.ImageField(upload_to="web/engi")
    



    class Meta:
        db_table = 'web_designs'
        verbose_name = "designs"
        verbose_name_plural = "designs"

    def __unicode__(self):
        return self.title


class pharma(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    contents = models.URLField(default="", editable=True)
    phone = models.TextField()
    image = models.ImageField(upload_to="web/engi")
    



    class Meta:
        db_table = 'web_pharma'
        verbose_name = "pharma"
        verbose_name_plural = "pharma"

    def __unicode__(self):
        return self.title



class veti(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    contents = models.URLField(default="", editable=True)
    phone = models.TextField()
    image = models.ImageField(upload_to="web/engi")
    


    class Meta:
        db_table = 'web_veti'
        verbose_name = "veti"
        verbose_name_plural = "veti"

    def __unicode__(self):
        return self.title


class contact(models.Model):
    title = models.CharField(max_length=128)


    class Meta:
        db_table = 'web_contact'
        verbose_name = "contact"
        verbose_name_plural = "contact"

    def __unicode__(self):
        return self.title


class resource(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    website = models.URLField(default="", editable=True)
    

    class Meta:
        db_table = 'web_resource'
        verbose_name = "resource"
        verbose_name_plural = "resource"

    def __unicode__(self):
        return self.title



class mass(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    contents = models.URLField(default="", editable=True)
    phone = models.TextField()
    image = models.ImageField(upload_to="web/engi")
    


    class Meta:
        db_table = 'web_mass'
        verbose_name = "mass"
        verbose_name_plural = "mass"

    def __unicode__(self):
        return self.title