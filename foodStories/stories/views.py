from django.shortcuts import render,redirect
from django.http import HttpResponse
from stories.forms import ContactForm, SubscribeForm, StoryForm, LoginForm
from django.views import View
# from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from stories.models import Recipe, Story
# Create your views here.


def home(request):
    return render( request , 'index.html')

def about(request):
    return render( request , 'about.html')

# def create_story(request):
#     return render(request, 'create_story.html')

class StoryView(View):
    template_name = 'create_story.html'
    form_class = StoryForm
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form' : form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return render(request, self.template_name, {'form' : form})


# def stories(request):
#     return render( request , 'stories.html')

class StoryList(ListView):
    model = Story
    context_object_name = 'stories'
    template_name='stories.html'

class StoryDetail(DetailView):
    model = Story
    context_object_name = 'context'
    template_name='single.html'

# def recipes(request):
#     return render( request , 'recipes.html')

class RecipeList(ListView):
    model = Recipe
    context_object_name = 'recipes'
    template_name='recipes.html'

class RecipeDetail(DetailView):
    model = Recipe
    context_object_name = 'context'
    template_name='single.html'

def login(request):
    return render(request, 'accounts/login.html' )

class LoginView(View):
    template_name = 'accounts/login.html'
    form_class = LoginForm
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name , {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            pass
        return render(request, self.template_name, {'form': form})

def register(request):
    return render(request, 'accounts/register.html' )

def single(request):
    return render(request, 'single.html')

def reset_password(request):
    return render(request, 'accounts/reset_password.html')

def change_password(request):
    return render(request, 'accounts/change_password.html')
    
def forget_password(request):
    return render(request, 'accounts/forget_password.html')

def user_profile(request):
    return render(request, 'user_profile.html')

def email_subscribers(request):
    return render(request, 'email_subscribers.html')



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ContactForm()
        
    return render( request , 'contact.html', {'form': form})

class ContactView(View):
    template_name = 'contact.html'
    form_class = ContactForm
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render( request , self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        # print(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            print(name)
            form.save()
            return redirect('/')
        
        return render( request , self.template_name, {'form': form})


def subscribe(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SubscribeForm()
    
    return render(request , 'subscribe.html' , {'form' : form})

class SubscribeView(View):
    form_class = SubscribeForm
    template_name = 'subscribe.html'
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request , self.template_name , {'form' : form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(request , 'subscribe.html' , {'form' : form})