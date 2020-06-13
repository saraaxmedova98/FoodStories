from django.shortcuts import render
from django.http import HttpResponse
from stories.forms import ContactForm, SubscribeForm
# Create your views here.


def home(request):
    return render( request , 'index.html')

def about(request):
    return render( request , 'about.html')

def stories(request):
    return render( request , 'stories.html')

def recipes(request):
    return render( request , 'recipes.html')

def login(request):
    return render(request, 'accounts/login.html' )

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

def create_story(request):
    return render(request, 'create_story.html')

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

def subscribe(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SubscribeForm()
    
    return render(request , 'subscribe.html' , {'form' : form})