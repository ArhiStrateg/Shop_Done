from django import forms


class CheckoutContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone = forms.IntegerField(required=True)
    adress = forms.CharField(required=True)
    comment = forms.CharField(required=False)


class Find_Project_Form(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone = forms.IntegerField(required=True)
    adress = forms.CharField(required=True)
    comment = forms.CharField(required=False)
    project = forms.FileField(required=False)

