from django import forms
from .models import Image
from .models import Employee


#class ImageForm(forms.ModelForm):
#    """Form for the image model"""
#    class Meta:
#       model = Image
#       fields = ('title', 'image')

class EmployeeForm(forms.ModelForm): 
    class Meta: 
        model = Employee 
        fields = ['name', 'emp_image'] 