__author__ = 'penhagonzalez'

from django import forms

class FormComite(forms.Form):
   # proyecto = forms.(Proyecto, related_name='proyecto')
   # miembros = models.ForeignKey(Usuario)
    miembro_uno = forms.CheckboxFieldRenderer(Usuario)                    #
    miembro_dos = forms.ForeignKey(Usuario)
    miembro_tres = forms.ForeignKey(Usuario)