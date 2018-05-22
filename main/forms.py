from django import forms
from main.models import Search_Low


class Search_Low_Form(forms.ModelForm):
    class Meta:
        model = Search_Low
        exclude = [""]

class Login_Form(forms.Form):
    login = forms.CharField()
    password = forms.CharField(min_length=3, max_length=20, widget=forms.TextInput(attrs={"type": "password"}))
