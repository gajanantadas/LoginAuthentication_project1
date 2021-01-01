from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
class SignUpForm(UserCreationForm): #inheriting UserCreationForm then all the functionality avilable to u class
    password2 = forms.CharField(label='Conform Password(again)', widget=forms.PasswordInput)#change the lable name for that
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'email': 'Email'}#for changeing lable name thats why used

class EditUserForm(UserChangeForm):
    password = None
    class Meta :
        model = User
        fields = ['username','first_name','last_name','email','is_active','date_joined']
        labels = {'email':'Email'}
