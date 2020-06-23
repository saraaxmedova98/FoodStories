from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import  CreateView, UpdateView
from django.contrib.auth import get_user_model
from account.forms import RegisterForm, LoginForm, UserEditForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import LoginView
from stories.models import Recipe, Story

# Create your views here.

User = get_user_model()

class CreateRegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('account:login')

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

class UserLoginView(LoginView):
    template_name = 'registration/login.html'
    form_class = LoginForm

    # def get_success_url(self,**kwargs):
    #     return reverse_lazy('stories:home')


class UserProfileView(TemplateView):
    template_name = "user_profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print()
        context["user_profile"] = User.objects.get(email=self.request.user)
        context["user_recipes"] = Recipe.objects.filter(users = self.request.user)
        context["user_stories"] = Story.objects.filter(user = self.request.user)
        return context
    


