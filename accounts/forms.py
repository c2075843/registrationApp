from django import forms
from django.contrib.auth.models import User,Group
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Student

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label = 'Email address', help_text = 'Your email address.')
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
     email = forms.EmailField()
     
     class Meta:
          model = User
          fields = ['first_name', 'last_name', 'email']

   
class ProfileUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)
    photo = forms.ImageField(required=False)
     
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'photo']
          
