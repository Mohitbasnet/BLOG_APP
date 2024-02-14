from django import forms
from django.contrib.auth.models import User
class LoginForm(forms.Form):
    username = forms.CharField(max_length = 30)
    password = forms.CharField(widget=forms.PasswordInput())





class UserRegistration(forms.ModelForm):
    password = forms.CharField(label = 'password', widget = forms.PasswordInput)
    password2 = forms.CharField(label = 'Confirm Password', widget = forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):

        cd = self.cleaned_data

        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Password dont match')

        return cd['password2']

        



