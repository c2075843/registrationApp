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
    photo = forms.ImageField(required=False)
    course=forms.ModelChoiceField(queryset=Group.objects.all(),empty_label="Choose a course")
     
    class Meta:
        model = Student
        fields = ['photo', 'course']
          
