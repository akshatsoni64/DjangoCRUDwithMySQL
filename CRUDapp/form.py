from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'max_length': '30',
            'placeholder': 'Name Here...'
        }
    ))
    branch = forms.CharField(widget=forms.TextInput(
        attrs={
            'max_length': '20',
            'placeholder': 'Branch Here...'
        }
    ))
    eno = forms.CharField(widget=forms.TextInput(
        attrs={
            'max_length': '10',
            'placeholder': 'Enrollment Number Here...'
        }
    ))

    class Meta:
        model = Student
        fields = '__all__'
