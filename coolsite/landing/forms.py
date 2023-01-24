from django import forms
from .models import Client


class Clients_phone(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email_client', 'phone', 'date_meeting', 'place_meeting', 'topic_meeting', 'comment_client']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email_client': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'date_meeting': forms.TextInput(attrs={'class': 'form-control'}),
            'place_meeting': forms.TextInput(attrs={'class': 'form-control'}),
            'topic_meeting': forms.TextInput(attrs={'class': 'form-control'}),
            'comment_client': forms.TextInput(attrs={'class': 'form-control'}),

        }
