from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import  CreateView, UpdateView,FormMixin
from django.contrib.auth import get_user_model
from account.forms import *
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView,\
    PasswordResetConfirmView
from stories.models import *
from django.shortcuts import redirect
# Create your views here.

User = get_user_model()

class CreateRegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('account:login')

    # def dispatch(self, request, *args, **kwargs):
    #     """
    #     Check that user signup is allowed before even bothering to
    #     dispatch or do other processing.

    #     """
    #     if request.user.is_authenticated:
    #         return redirect('stories:home')
    #     if not self.registration_allowed(request):
    #         return redirect(self.disallowed_url)
    #     return super(RegistrationView, self).dispatch(request, *args, **kwargs)


    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, 'Something went wrong!!')
        return super().form_invalid(form)

class UpdateUserView(UpdateView):
    model = User
    form_class = UserEditForm
    template_name = 'update_user_info.html'

    def get_success_url(self):
        return reverse_lazy('account:user_profile', kwargs={'pk': self.object.pk})

class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = LoginForm
    success_url = reverse_lazy("stories:home")

class UserPasswordChangeView(PasswordChangeView):
    # models = User
    form_class = UserPasswordChangeForm
    template_name = 'accounts/change_password.html'
    success_url = reverse_lazy('account:password_change_done')


class UserPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = "accounts/pasword_change_done.html"


class UserPasswordResetView(PasswordResetView):
    form_class = ResetPasswordForm
    template_name = 'accounts/forget_password.html'
    email_template_name = 'accounts/password_reset_email.html'
    success_url = reverse_lazy('account:login')

class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'accounts/reset_password.html'
    form_class = CustomResetPasswordForm
    success_url = reverse_lazy("account:login")


class UserProfileView(FormMixin, DetailView):
    model = User
    template_name = "user_profile.html"
    form_class = ProfileSearchForm
        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        form = self.form_class(self.request.GET)
        if form.is_valid():
            context['user_stories'] = Story.objects.filter(user = self.request.user).filter(title__icontains=form.cleaned_data['name'])
            context['user_recipes'] = Recipe.objects.filter(user = self.request.user).filter(title__icontains=form.cleaned_data['name'])
        
        else:
            context["user_stories"] = Story.objects.filter(user = self.request.user)
            context["user_recipes"] = Recipe.objects.filter(user = self.request.user)
        return context
    


