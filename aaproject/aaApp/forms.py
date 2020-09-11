from django import forms
from aaApp.models import Student

# create your form view here.
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

