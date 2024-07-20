from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

from .models import Customer_Picture,Comment

class LoginForm(AuthenticationForm) :
    
    class Meta :
        model = User
        fields = ("username", "password")
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input'}),
            'password': forms.PasswordInput(attrs={'class': 'input'}),
            
        }


class CreateUserForm(UserCreationForm) :
    
    
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user




class ImageForm(forms.ModelForm) :

    class Meta :

        model = Customer_Picture
        fields = ("photo","description","category")





class Comment_Form(forms.ModelForm) :

    class Meta :

        model = Comment
        fields = ('comment_body',)





##########################################################################################
    # class Meta :
    #     model = User
    #     fields = ['username','email','password1','password2']
    #     widgets = {
    #         'username': forms.TextInput(attrs={'class': 'input','name' : 'username'}),
    #         'email': forms.EmailInput(attrs={'class': 'input','name' : 'email'}),
    #         'password1' : forms.PasswordInput(attrs={'id': 'pass','name' : 'password'}),
    #         'password2' : forms.PasswordInput(attrs={'class': 'input',}),
    #     }
#######################################################################################   

