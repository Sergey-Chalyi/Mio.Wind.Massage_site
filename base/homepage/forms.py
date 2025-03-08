from django import forms

from homepage.models import VisitRecord


class AddVisitRecordForm(forms.ModelForm):
    class Meta:
        model = VisitRecord
        fields = ['customer_name', 'customer_tel', 'customer_comment', 'to_specialist']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': "Ім'я",
        })
        self.fields['customer_tel'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': "Номер телефону",
        })
        self.fields['customer_comment'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Коментар',
        })

        self.fields['to_specialist'].widget.attrs.update({
            'style' : 'display: none'
        })