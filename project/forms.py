from django import forms
from .models import Employee

from .models import Image
from .models import Folder
from .models import Task
from .models import User


class EmployeeForm(forms.ModelForm): 
    class Meta: 
        model = Employee 
        fields = ['name', 'emp_image'] 

class ImageForm(forms.ModelForm): 
    class Meta: 
        model = Image
        fields = ['folder','filename', 'imageFile', 'index'] 

class FolderForm(forms.ModelForm): 
    class Meta: 
        model = Folder
        fields = ['folder','sex'] 

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['folder','indexStop', 'user', 'order'] 


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','password', 'sexAssign', 'order', 'tasksDone'] 

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','password']

class MassUsersForm(forms.Form):
    numberUsers = forms.IntegerField()