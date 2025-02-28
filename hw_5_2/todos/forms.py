from django import forms

class TodoListForm(forms.Form):
    title = forms.CharField(min_length=5, max_length=200, required=True, widget=forms.TextInput({
        'class': 'form-control',
        'placeholder': 'Enter todo list title'
    }))
    description = forms.CharField(min_length=5, max_length=200, required=True, widget=forms.TextInput({
        'class': 'form-control',
        'placeholder': 'Enter todo list description'
    }))

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

class EditTodoForm(forms.Form):
    title = forms.CharField(min_length=5, max_length=200, required=True, widget=forms.TextInput({
        'class': 'form-control',
        'placeholder': 'Enter todo title'
    }))
    description = forms.CharField(min_length=5, max_length=200, required=True, widget=forms.TextInput({
        'class': 'form-control',
        'placeholder': 'Enter description'
    }))

    due_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    status = forms.BooleanField(required=False)

    todo_list_id = forms.IntegerField(min_value=1, max_value=1000000, required=True, widget=forms.TextInput({
        'class': 'form-control',
        'placeholder': 'Select todo_list'
    }))