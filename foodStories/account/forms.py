from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm,\
    PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django import forms
from account.models import CustomUser
from django.contrib.auth import get_user_model
# Register your forms here.

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email',)

class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        widgets = {
             'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'First name'
            }),
             'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Last name'
            }),
             'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Username'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Email'
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Password'
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Confirm Password'
            }),
            
        }

class UserEditForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ("first_name",'last_name','username','email','bio','profile_image')
        widgets = {
             'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'First name'
            }),
             'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Last name'
            }),
             'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Username'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Email'
            }),
            'bio': forms.Textarea(attrs={
                'class': 'form-control resize',
                'placeholder' : 'Biography'
            }),
            
        }



class LoginForm(AuthenticationForm):
    username = forms.EmailField(widget = forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder' : 'Email'
    }), required=True)
    password = forms.CharField(widget= forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder' : 'Password'
    }), required=True)

class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget = forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder' : 'Old Password'
    }), required=True)
    new_password = forms.CharField(widget = forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder' : 'New Password'
    }), required=True)
    confirm_new_password = forms.CharField(widget = forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder' : 'Cinfirm Password'
    }), required=True)

    class Meta:
        fields = ('old_password', 'new_password', 'confirm_new_password', )


class ResetPasswordForm(PasswordResetForm):
    email = forms.EmailField(widget = forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder' : 'Email'
    }), required=True)

class CustomResetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(widget = forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder' : 'Password'
    }), required=True)
    new_password2 = forms.CharField(widget = forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder' : 'Password 2'
    }), required=True)

