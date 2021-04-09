from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django import forms
    
class CustomSignupForm(UserCreationForm):
    email=forms.EmailField(max_length=254, help_text='Needed to verify email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text='Your password must contain 8 character.'
    
    def clean_password1(self):
        password1=self.cleaned_data.get('password1')
        if len(password1)<8:
            raise ValidationError('Password must contain 8 character.')
        return password1
    