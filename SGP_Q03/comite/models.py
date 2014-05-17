__author__ = 'penhagonzalez'
from django.db import models

from usuarios.models import Usuario
from proyectos.models import Proyecto


class Comite(models.Model):
    codigo=models.AutoField(primary_key=True)
    proyecto = models.ForeignKey(Proyecto, related_name='proyecto')
    miembros = models.ManyToManyField(Usuario)
    miembro_uno = models.ForeignKey(Usuario)                    #
    #miembro_dos = models.ForeignKey(Usuario)
    #miembro_tres = models.ForeignKey(Usuario)
    def __unicode__(self):
        return self.codigo

        """ from django.db import models
from django.forms.models import ModelForm
from django.forms.widgets import CheckboxSelectMultiple

class Company(models.Model):
    industries = models.ManyToManyField(Industry, blank=True, null=True)

class CompanyForm(ModelForm):

    class Meta:
        model = Company
        fields = ("industries")

    def __init__(self, *args, **kwargs):

        super(CompanyForm, self).__init__(*args, **kwargs)

        self.fields["industries"].widget = CheckboxSelectMultiple()
        self.fields["industries"].queryset = Industry.objects.all()  """