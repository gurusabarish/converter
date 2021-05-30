from django import forms


class files(forms.Form):
    docs = forms.FileField()
