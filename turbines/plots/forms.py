from django import forms


class InputForm(forms.Form):
    start = forms.CharField(label='start', max_length=20)
    end = forms.CharField(label='end', max_length=20)
