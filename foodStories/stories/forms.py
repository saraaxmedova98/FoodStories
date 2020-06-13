from django import forms
from django.forms import ModelForm
from stories.models import Contact, Subscribe



class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ("name", 'email', 'subject', 'message')
        widgets={
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Your Name'}),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Your Email'}),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Subject'}),
            'message': forms.Textarea(attrs={
                'class': 'form-control resize',
                'placeholder' : 'Message'}),
            
            
        }

class SubscribeForm(forms.ModelForm):
    
    class Meta:
        model = Subscribe
        fields = ("email",)
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder' : 'Enter email address'
                }
            )
        }
