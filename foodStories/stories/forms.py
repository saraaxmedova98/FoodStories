from django import forms
from django.forms import ModelForm
from stories.models import Contact, Subscribe, Story, Recipe, Comment, StoryImage
from django.core.mail import send_mail  

class StoryForm(forms.ModelForm):
    
    class Meta:
        model = Story
        fields = ("title",'description', 'category','tags', 'story_image',)
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control resize',
                'placeholder' : 'Description'
            }),
            'tags': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Tags',
                'data-role': 'tagsinput'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
            }),
            'thumbnail': forms.FileInput(attrs={
                'class': 'form-control',
                'multiple': True
            })
            # 'story_image': forms.ClearableFileInput()

        }
       
# class StoryImageForm(forms.ModelForm):
    # file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))


class RecipeForm(forms.ModelForm):
    
    class Meta:
        model = Recipe
        fields = ("title",'description','ingredients', 'category','prepare_time', 'recipe_image')
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
            'prepare_time': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Prepare time'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
            })
            
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

class SumForm(forms.Form):
    x = forms.IntegerField( required=False)
    y = forms.IntegerField( required=False)
    
