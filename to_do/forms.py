from django import forms

from .models import Tasks


class CreateTaskForm(forms.ModelForm):
    # name = forms.CharField(
    #     label = "Tarea",
    #     error_messages=[
    #         'unique':
    #     ],
    #     widget = forms.TextInput( attrs={'class': 'form-control'} ))
    # priority = forms.CharField(label = "Prioridad", widget = forms.Select(choices=(('L', 'BAJO'), ('M', 'MEDIO'), ('H', 'ALTO')), attrs={'class': 'form-select'} ))
    # description = forms.CharField(label = "Description", widget = forms.Textarea( attrs={'class': 'form-control', 'rows': '5'} ))
    # year = forms.CharField(label = "Year", widget = forms.NumberInput( attrs={'class': 'form-control'} ))
    class Meta:
        model = Tasks
        fields = [
            'name', 'priority',
        ]
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'priority': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
        }
        error_messages = {
            'unique': 'blaaaa'
        }

    # def clean(self):
    #     super().clean()

    #     name = self.cleaned_data.get('name')

    #     if len(name)<5:
    #         self.add_error('name','Can not save name less than 5 characters long')
    #         self.fields['name'].widget.attrs.update({'class': 'form-control  is-invalid'})
    #         print('Name must be more than 3 characters CLEAN')
    #     return self.cleaned_data
        # return name

    def clean_name(self):
        # super().clean()
        name = self.cleaned_data.get('name')

        if len(name) < 3:
            self.add_error('name','La tarea debe tener más de tres caracteres')
            self.fields['name'].widget.attrs.update({'class': 'form-control is-invalid'})
            print('Name must be more than 3 characters NAME')
        if Tasks.objects.filter(name=name).exists():
            self.add_error('name', f'Ya existe una tarea con el mismo nombre {name}.')
            self.fields['name'].widget.attrs.update({'class': 'form-control is-invalid'})
            print(f'Ya existe una tarea con el mismo nombre {name}.')
        return name
