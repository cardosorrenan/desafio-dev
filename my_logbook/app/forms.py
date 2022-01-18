from django import forms

class UploadCNABForm(forms.Form):
    cnab_file = forms.FileField()