from django import forms
from django.forms import ModelForm
from stories.models import Contact, Subscribe, Story

class StoryForm(forms.ModelForm):
    
    class Meta:
        model = Story
        fields = ("title",'description', 'category', 'story_image',)
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder' : 'Description'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
            })
            # 'story_image': forms.ClearableFileInput()

        }


class ContactForm(forms.ModelForm):
    
    class Meta:
        source = forms.CharField( max_length=50, required=False, widget=forms.HiddenInput())
        model = Contact
        fields = ("name", 'email', 'subject', 'message','source')
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

class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    email.widget = forms.EmailInput(attrs={'class': 'form-control','placeholder' : 'Username'})
    password = forms.CharField(max_length=50, required=True)
    password.widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder' : 'Password'})
    remember = forms.BooleanField(label='Check me out',required=False)


    
