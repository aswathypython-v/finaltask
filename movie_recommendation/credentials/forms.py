from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.core.exceptions import ValidationError

class UserForm(UserCreationForm):
    username=forms.CharField(label='username')
    email = forms.EmailField(label='email')
    first_name=forms.CharField(label='firstname')
    last_name=forms.CharField(label='lastname')

    class Meta:
        model=User
        fields=('username','first_name','last_name','email')

    def clean_password(self):
        password=self.cleaned_data('password')
        password1=self.cleaned_data('password1')

        if password and password1 and password!=password1:
            raise ValidationError("password doesn't match")
        return password1

class UpdateUserForm(UserChangeForm):
    email = forms.EmailField(label='email')
    first_name=forms.CharField(label='firstname')
    last_name=forms.CharField(label='lastname')

    class Meta:
        model=User
        fields=('username','first_name','last_name','email')
