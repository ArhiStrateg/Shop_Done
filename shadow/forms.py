from django import forms


class Project_Form_For_Shadow(forms.Form):
    comment = forms.CharField(required=False)
    project = forms.FileField(required=False)

class Order_Form_For_Shadow(forms.Form):
    comment = forms.CharField(required=False)
    order = forms.FileField(required=False)