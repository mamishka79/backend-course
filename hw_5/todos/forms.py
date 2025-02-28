from django import forms

class StudentCreationForm(forms.Form):
    title = forms.CharField(min_length=5, max_length=200, required=True, widget=forms.TextInput({
        'class': 'form-control',
        'placeholder': 'Enter title'
    }))
    description = forms.CharField(min_length=5, max_length=200, required=True, widget=forms.TextInput({
        'class': 'form-control',
        'placeholder': 'Enter description'
    }))
    due_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    status = forms.BooleanField(required=False)