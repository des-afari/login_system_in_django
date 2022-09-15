from django import forms 

class RegistrationForm(forms.Form):
    first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'First name'}))
    last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password_check = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Re-enter password'}))

