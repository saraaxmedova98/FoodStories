from django.shortcuts import render,redirect
from django.http import HttpResponse
from stories.forms import ContactForm, SubscribeForm, StoryForm, LoginForm
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView
from stories.models import Recipe, Story, Category, Tag, Author
from django.db.models import Count
# Create your views here.


# def home(request):
#     return render( request , 'index.html')

class HomeView(TemplateView):
    template_name = "index.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recipes"] = Recipe.objects.all()[:2]
        context['stories'] = Story.objects.all()[:4]
        context['categories'] = Category.objects.all()[:3]
        return context
    

# def about(request):
#     return render( request , 'about.html')

class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recipes"] = Recipe.objects.annotate(Count('title'))
        context['stories'] = Story.objects.annotate(Count('title'))
        context['categories'] = Category.objects.all()[:3]
        context['authors'] = Author.objects.annotate(Count('first_name'))
        return context
    

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()[:3]
        return context


class StoryCategoryList(ListView):
    context_object_name = 'stories'
    template_name='stories.html'

    def get_queryset(self):
        self.category = get_object_or_404(Category, title=self.kwargs['category'])
        return Story.objects.filter(category=self.category)

class StoryDetail(DetailView):
    model = Story
    context_object_name = 'story'
    template_name='story_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context['tags'] = Tag.objects.all()
        context['stories'] = Story.objects.all()[:3]
        return context
    

# def recipes(request):
#     return render( request , 'recipes.html')

class RecipeList(ListView):
    model = Recipe
    context_object_name = 'recipes'
    template_name='recipes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()[:3]
        return context
    

class RecipeDetail(DetailView):
    model = Recipe
    context_object_name = 'recipe'
    template_name='recipe_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context['tags'] = Tag.objects.all()
        context['recipes'] = Recipe.objects.all()[:3]
        return context

# def login(request):
#     return render(request, 'accounts/login.html' )

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

# class CatStorList(ListView):
#     model = Category
#     context_object_name = ''
#     template_name=''


# def subscribe(request):
#     if request.method == 'POST':
#         form = SubscribeForm(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form = SubscribeForm()
    
#     return render(request , 'subscribe.html' , {'form' : form})

class SubscribeView(View):
    form_class = SubscribeForm
 
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()

       

  