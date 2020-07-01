from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from stories.forms import ContactForm, SubscribeForm, StoryForm, RecipeForm, CommentForm, SumForm
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView
from stories.models import Recipe, Story, Category, Contact, Comment, SumNumbers, Subscribe
from account.models import CustomUser
from django.db.models import Count
from django.utils import timezone
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView, FormMixin
from django.core.mail import send_mail
from django.contrib import messages
from django.urls import reverse_lazy
from taggit.models import Tag 
from django.template.defaultfilters import slugify
from django.contrib.auth import get_user_model
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from stories.api.serializers import StoryModelSerializer
from stories.tasks import add , subscribers_email
# Create your views here.

User = get_user_model()

class HomeView(TemplateView):
    template_name = "index.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.request.user)
        if self.request.user.is_authenticated:
            
            context["recipes"] = Recipe.objects.all()[:2]
            context['stories'] = Story.objects.all()[:4]
            context['user_stories'] = Story.objects.filter(user = self.request.user)[:3]
            context['categories'] = Category.objects.all()[:3]
            context['user_profile'] = User.objects.get(email = self.request.user)
            return context
        else:
            return reverse_lazy('account:login')
    

class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recipes"] = Recipe.objects.all()
        context['stories'] = Story.objects.all()
        context['categories'] = Category.objects.all()[:3]
        # context['authors'] = Author.objects.all()
        return context


class StoryCreateView(CreateView):
    model = Story
    template_name = "create_story.html"
    # fields = ['title', 'description', 'story_image', 'category']
    form_class = StoryForm
    def form_valid(self, form):
        form.instance.user = self.request.user
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
    success_url = reverse_lazy('stories:stories')


class StoryList(ListView):
    model = Story
    context_object_name = 'stories'
    template_name='stories.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()[:3]
        context['user'] = User.objects.get(email = self.request.user)
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
    def get_success_url(self):
        return reverse_lazy('stories:story_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context['stories'] = Story.objects.all()[:3]
        context['tags']= Story.tags.most_common()
        
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
        print("salam")
        # print(self.request.user.profile.whatever)
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
        form.instance.user = self.request.user
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
    success_url = reverse_lazy('stories:recipes')



class ContactCreateView(CreateView):
    model = Contact
    template_name = "contact.html"
    form_class = ContactForm
    success_url = reverse_lazy('stories:home')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, 'Something went wrong!!')
        return super().form_invalid(form)


class SubscribeView(FormView):
    model = Subscribe
    template_name = "subscribe.html"
    success_url = reverse_lazy('stories:home')
    form_class = SubscribeForm
    
    def form_valid(self, form):
        # form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, 'Something went wrong!!')
        return super().form_invalid(form)



class EmailSubscribeView(View):
    def get(self, request, *args, **kwargs):
        subscribers_email.delay()
        return HttpResponse('<h1>Email send successfully to subscribers</h1>')



@csrf_exempt
def story_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        story = Story.objects.all()
        serializer = StoryModelSerializer(story, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StoryModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)     


@csrf_exempt
def story_detail(request, pk):
    """
    Retrieve, update or delete a code story.
    """
    try:
        story = Story.objects.get(pk=pk)
    except Story.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = StoryModelSerializer(story)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = StoryModelSerializer(story, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        story.delete()
        return HttpResponse(status=204)

class SumCreateView(FormView):
    model = SumNumbers
    template_name = "sum.html"
    success_url = reverse_lazy('stories:sum')
    # fields = ['title', 'description', 'story_image', 'category']
    form_class = SumForm
    def form_valid(self, form):
        x = form.cleaned_data['x']
        y = form.cleaned_data['y']
        result = add.delay(x,y)
        print(x,y, result)
        SumNumbers.objects.create(sum = result.get())
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, 'Something went wrong!!')
        return super().form_invalid(form)
