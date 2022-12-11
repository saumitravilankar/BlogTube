from django import forms
from .models import Profile,User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):

    class Meta():
        model = User
        fields = ('username','email','password1','password2')

class AdditionalInfoForm(forms.ModelForm):

    class Meta():
        model = Profile
        fields = ('profile_pic',)