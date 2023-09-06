from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm





class RegistratioinForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
        help_texts = {
            'username': None,
            'email': None,
            'password1':None,
        }
        

        
 
class LoginForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username']
        help_texts = {
            'username': None,
            'email': None,
            'password1':None,
        }
      
class ProfileForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'
        


