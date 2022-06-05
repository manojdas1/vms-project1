from django import forms
from .models import User

class VaccineRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['Aadhaar_Number', 'Name', 'Age', 'Gender', 'Mobile_Number', 'Dose', 'Vaccine_Name']
        widgets = {
            'Aadhaar_Number': forms.NumberInput(attrs={'class':'form-control'}),
            'Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Age': forms.NumberInput(attrs={'class': 'form-control'}),
            'Gender': forms.TextInput(attrs={'class': 'form-control'}),
            'Mobile_Number': forms.NumberInput(attrs={'class': 'form-control'}),
            'Dose': forms.NumberInput(attrs={'class': 'form-control'}),
            'Vaccine_Name': forms.TextInput(attrs={'class': 'form-control'}),
        }