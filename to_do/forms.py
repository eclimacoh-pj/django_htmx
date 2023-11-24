from django import forms

from .models import Tasks


class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = [
            'name', 'priority',
        ]
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-class'
                }
            ),
            'priority': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
        }

    def clean(self):
        super(CreateTaskForm, self).clean()
        name = self.cleaned_data.get('name')
        if len(name) <= 3:
            self.add_error('name', 'add_error')
            self.fields['name'].widget.attrs.update({'class': 'form-control is-invalid'})
            raise forms.ValidationError('Name must be more than 3 characters')
        return self.cleaned_data

