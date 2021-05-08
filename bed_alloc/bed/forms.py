from django import forms
from .models import Register


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['fname', 'lname', 'email', 'mobile', 'age', 'ct', 'oxy', 'oc', 'ct_pdf']