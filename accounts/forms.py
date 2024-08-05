from typing import Any
from django import forms
from . models import Account


class RegistrationForm(forms.ModelForm):
    
    password=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Enter Password',
        'class':'form-control',#for adding style for the input field the form-control is the bootstrap class for one input

    }))
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Confirm Password'
    }))
    class Meta:
        model=Account
        fields=['first_name','last_name','phone_number','email','password']



    def clean(self):
        cleaned_data=super(RegistrationForm,self).clean()
        password=cleaned_data.get('password')
        confirm_password=cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                'Password does not match!!'
            )

    def __init__(self,*args, **kwargs):
        super(RegistrationForm,self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] ='Enter your first name'
        self.fields['last_name'].widget.attrs['placeholder'] ='Enter your last name'
        self.fields['phone_number'].widget.attrs['placeholder'] ='Enter your phone number'
        self.fields['email'].widget.attrs['placeholder'] ='Enter email id'
        for field in self.fields:# this code is used for to apply the bootstrap class for all the form input field
            self.fields[field].widget.attrs['class'] ='form-control'