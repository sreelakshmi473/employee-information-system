from django import forms
from work.models import Employees,Department,Position
from django.contrib.auth.models import User

class Employeeform(forms.ModelForm):
       
    class Meta:
        model = Employees
        fields = '__all__'

        widgets = {
                    "name":forms.TextInput(attrs={"class":"forms-control"}),
                    "place":forms.TextInput(attrs={"class":"forms-control"}),
                    "course":forms.TextInput(attrs={"class":"forms-control"}),
                    "age":forms.TextInput(attrs={"class":"forms-control"}),
                    "gender":forms.TextInput(attrs={"class":"forms-control"}),
            }

class Register(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','first_name','last_name','email']

class Signin(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

class Departmentform(forms.ModelForm):
    class Meta:
        model=Department
        fields = "__all__"


class Positionform(forms.ModelForm):
    class Meta:
        model=Position
        fields= "__all__"