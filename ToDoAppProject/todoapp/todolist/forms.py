from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from todolist.models import TODO





class CreateUserForm(UserCreationForm):
    email =  forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name =  forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name =  forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['class']='form-control'


class TODOForm(ModelForm,forms.Form):
    class Meta:
        model=TODO
        fields=['title','priority','status','last_date']



