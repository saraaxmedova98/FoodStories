from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from stories.forms import ContactForm, SubscribeForm, StoryForm, RecipeForm, CommentForm
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView
from stories.models import Recipe, Story, Category, Tag, Contact, Comment
from django.db.models import Count
from django.utils import timezone
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView, FormMixin
from django.core.mail import send_mail
from django.contrib import messages
from django.urls import reverse_lazy
from taggit.models import Tag 
# Create your views here.


class HomeView(TemplateView):
    template_name = "index.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recipes"] = Recipe.objects.all()[:2]
        context['stories'] = Story.objects.all()[:4]
        context['categories'] = Category.objects.all()[:3]
        return context
    

class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recipes"] = Recipe.objects.all()
        context['stories'] = Story.objects.all()
        context['categories'] = Category.objects.all()[:3]
        context['authors'] = Author.objects.all()
        return context


class StoryCreateView(CreateView):
    model = Story
    template_name = "create_story.html"
    # fields = ['title', 'description', 'story_image', 'category']
    form_class = StoryForm
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, 'Something went wrong!!')
        return super().form_invalid(form)

class StoryUpdateView(UpdateView):
    model = Story
    template_name = "create_story.html"
    form_class = StoryForm

class StoryDeleteView(DeleteView):
    model = Story
    template_name = "delete_story.html"
    success_url = reverse_lazy('stories')


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()[:3]
        return context

    def get_queryset(self):
        self.category = get_object_or_404(Category, title=self.kwargs['category'])
        return Story.objects.filter(category=self.category)
        # return Story.objects.filter(category=self.kwargs['category'])

class StoryDetail(FormMixin,DetailView):
    model = Story
    context_object_name = 'story'
    template_name='story_detail.html'
    form_class = CommentForm
    # common_tags = Post.tags.most_common()[:4]

    def get_success_url(self):
        return reverse_lazy('story_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context['stories'] = Story.objects.all()[:3]
        return context

    def get_object(self):
        story_count = super().get_object()
        story_count.story_count += 1
        story_count.save()
        return story_count
    
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class RecipeList(ListView):
    model = Recipe
    context_object_name = 'recipes'
    template_name='recipes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context


class RecipeCategoriesList(ListView):
   
    context_object_name = 'recipes'
    template_name='recipes.html'  


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()[:3]
        return context

    def get_queryset(self):
        self.category = get_object_or_404(Category, title=self.kwargs['category'])
        return Recipe.objects.filter(category=self.category)
    

class RecipeDetail(FormMixin ,DetailView):
    model = Recipe
    context_object_name = 'recipe'
    template_name='recipe_detail.html'
    form_class = CommentForm
    # success_url = reverse_lazy('self')

    # def get_queryset(self):
        # self.category = get_object_or_404(Category, title=self.kwargs['category'])
        # return Recipe.objects.filter(category=self.category)

    def get_success_url(self):
        return reverse_lazy('recipe_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context['recipes'] = Recipe.objects.all()[:3]
        return context

    def get_object(self):
        recipe_count = super().get_object()
        # Record the last accessed date
        recipe_count.recipe_count += 1
        recipe_count.save()
        return recipe_count

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class RecipeCreateView(CreateView):
    model = Recipe
    template_name = "create_recipe.html"
    form_class = RecipeForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, 'Something went wrong!!')
        return super().form_invalid(form)

class RecipeUpdateView(UpdateView):
    model = Recipe
    template_name = "create_recipe.html"
    form_class = RecipeForm


class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = "delete_recipe.html"
    success_url = reverse_lazy('recipes')



# class LoginView(View):
#     template_name = 'accounts/login.html'
#     form_class = LoginForm
#     def get(self, request, *args, **kwargs):
#         form = self.form_class()
#         return render(request, self.template_name , {'form': form})

#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             pass
#         return render(request, self.template_name, {'form': form})

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



class ContactCreateView(CreateView):
    model = Contact
    template_name = "contact.html"
    form_class = ContactForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, 'Something went wrong!!')
        return super().form_invalid(form)



class SubscribeView(View):
    form_class = SubscribeForm
    
 
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()



       

  