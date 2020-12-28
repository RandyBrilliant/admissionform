from django import forms
from regform.models import StudentData

# create a ModelForm


class StudentForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = StudentData
        fields = "__all__"
        widgets = {
            'address': forms.Textarea(attrs={'placeholder': 'e.g. Jalan Mahoni No. 16'}),
            'father_address': forms.Textarea(attrs={'placeholder': 'e.g. Jalan Mahoni No. 16'}),
            'mother_address': forms.Textarea(attrs={'placeholder': 'e.g. Jalan Mahoni No. 16'}),
            'guardian_address': forms.Textarea(attrs={'placeholder': 'e.g. Jalan Mahoni No. 16'}),
        }
