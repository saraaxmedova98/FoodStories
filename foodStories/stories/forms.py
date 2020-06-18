from django import forms
from django.forms import ModelForm
from stories.models import Contact, Subscribe, Story, Recipe, Comment
from django.core.mail import send_mail  

class StoryForm(forms.ModelForm):
    
    class Meta:
        model = Story
        tags = Story.objects.all()
        fields = ("title",'description', 'category', 'story_image',)
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control resize',
                'placeholder' : 'Description'
            }),
            'tag_list': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Tags'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
            })
            # 'story_image': forms.ClearableFileInput()

        }
       
            
class RecipeForm(forms.ModelForm):
    
    class Meta:
        model = Recipe
        fields = ("title",'description','ingredients','directions', 'category','prepare_time', 'recipe_image')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control resize',
                'placeholder' : 'Description'
            }),
            'ingredients': forms.Textarea(attrs={
                'class': 'form-control resize',
                'placeholder' : 'Ingredients'
            }),
            'directions': forms.Textarea(attrs={
                'class': 'form-control resize',
                'placeholder' : 'Directions'
            }),
            'prepare_time': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Prepare time'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
            })
            # 'story_image': forms.ClearableFileInput()

        }

    # def clean_title(self):
    #     title = self.cleaned_data["title"]
    #     recipe_exists = Recipe.objects.filter(title = title).exclude(pk = self.instance.pk)
    #     if self.instance and self.instance.pk and not recipe_exists:
    #         return title
    #     else:
    #         raise forms.ValidationError("Recipe already exists")
       

  
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

        # def send_mail(self)
        #     return('Subject here',
        #      'Here  the message.',
        #       'sara.axmedova98@gmail.com',
        #        ['sara.axmedova98@gmail.com'],
        #         fail_silently=False)
        # def send_email(self):
        #     'Subject',
        #     'Email message',
        #     'sara.axmedova98@gmail.com',
        #     ['sara.axmedova98@gmail.com'],
        #     fail_silently=False

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

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ("name",'email', 'message',)
        widgets={
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Your Name'}),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Your Email'}),
            'message': forms.Textarea(attrs={
                'class': 'form-control resize',
                'placeholder' : 'Message'}),            
        }



class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    email.widget = forms.EmailInput(attrs={'class': 'form-control','placeholder' : 'Username'})
    password = forms.CharField(max_length=50, required=True)
    password.widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder' : 'Password'})
    remember = forms.BooleanField(label='Check me out',required=False)


    
