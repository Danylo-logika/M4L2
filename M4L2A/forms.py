from django import forms
from M4L2A.models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name','email','date_in','date_out','phone']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Ваше ім'я"
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'email@example.com'
            }),
            'date_in': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'date_out': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+380...'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form'