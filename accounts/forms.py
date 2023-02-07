from django import forms
from .models import Account,UserProfile

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'enter password'
    }))

    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'confirm password'
    }))

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'password']
 
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'enter first name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'enter last name'
        self.fields['email'].widget.attrs['placeholder'] = 'enter email'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'enter phone number'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form_control'

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')  
        confirm_password = cleaned_data.get('confirm_password')   

        if password != confirm_password:
            raise forms.ValidationError(
                "password does not match!"
            )  


class UserForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('first_name','last_name','phone_number')
  
    def __init__(self, *args, **kwargs):
      super(UserForm,self).__init__(*args,**kwargs)  
      for field in self.fields:
          self.fields[field].widget.attrs['class'] = 'form-control' 

class UserprofileForm(forms.ModelForm):
    profile_picture = forms.ImageField(required=False, error_messages= {'invalid':("image files only")},widget=forms.FileInput)
    class Meta:
        model = UserProfile
        fields = ('address_line_1','address_line_2','city','state','country','profile_picture')

    def __init__(self, *args, **kwargs):
      super(UserprofileForm,self).__init__(*args,**kwargs)  
      for field in self.fields:
          self.fields[field].widget.attrs['class'] = 'form-control' 