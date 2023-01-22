from django import forms
from django.forms import ModelForm
from .models import Student


#create a form
class StudentForm(ModelForm):
    
    class Meta: 
        model = Student
        fields = ('First_name','Last_name','Email','Password','Confirm_Password','Select_Degree','Program_Of_Study','Graduation_year',)
        labels = {
            'First_name':'',
            'Last_name':'',
            'Email':'',
            'Password':'',
            'Confirm_Password':'',
            'Select_Degree':'',
            'Program_Of_Study':'',
            'Graduation_year':'',
        }
        widgets = {
            'First_name': forms.TextInput(attrs={'class':'form-control','placeholder':"First Name"}),
            'Last_name':forms.TextInput(attrs={'class':'form-control','placeholder': "Last Name"}),
            'Email':forms.EmailInput(attrs={'class':'form-control','placeholder':"Email"}),
            'Password':forms.PasswordInput(attrs={'class':'form-control','placeholder':"Password"}),
            'Confirm_Password':forms.PasswordInput(attrs={'class':'form-control','placeholder':"Confirm Password"}),
            'Program_Of_Study':forms.TextInput(attrs={'class':'form-control','placeholder':"Program Of Study"}),
            'Graduation_year':forms.DateInput(attrs={'class':'form-control','placeholder': "Graduation year"}),
        }

        
def clean(self):
    cleaned_data = super(StudentForm,self).clean()
    password = cleaned_data.get("Password")
    confirmed_password =cleaned_data.get('confirmed_password')

    if password != confirmed_password:
        raise forms.ValidationError(
            "passwords don't match"
                )
        return self.cleaned_data
