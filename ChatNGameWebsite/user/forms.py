from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=150)
    password = forms.CharField(label='Password', max_length=250)

class RegisterForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=250)
    username = forms.CharField(label='Username', max_length=150)
    password = forms.CharField(label='Password', max_length=250)
    confirm_password = forms.CharField(label='Confirm Password', max_length=250)
    
