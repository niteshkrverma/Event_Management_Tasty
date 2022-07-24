
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Contact
from django.core import validators
class SignUpForm(UserCreationForm):
    password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'email':'Email','first_name':'First Name','last_name':'Last Name'}
class ContactusForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.CharField()
    desc = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))
    phone=forms.CharField()

def mobile_no(value):
  mobile = str(value)
  if len(mobile) != 10:
    raise forms.ValidationError("Mobile Number Should 10 digit")
  
  
# class StuForm(forms.Form):
#   mob = forms.IntegerField(
#     validators =[mobile_no])
class BookingForm(forms.Form):

    Event_Name=forms.CharField(max_length=50)
    date=forms.DateField(required=False)
    Number=forms.NumberInput()

