from django import forms


class NewDepartamentoForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    departamento = forms.CharField(max_length=50)
    short_name = forms.CharField(max_length=20)

    

