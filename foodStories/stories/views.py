from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from stories.forms import ContactForm, SubscribeForm, StoryForm , RecipeForm, CommentForm, SumForm
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView
from stories.models import Recipe, Story, StoryImage, Category, Contact, Comment, SumNumbers,\
     Subscribe, TaggedStory
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
from account.forms import ProfileSearchForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

User = get_user_model()

class HomeView(FormMixin, TemplateView):
    template_name = "index.html"
    form_class = ProfileSearchForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.request.user)
        context['user_profile'] = User.objects.get_or_create(email = self.request.user)
        context['categories'] = Category.objects.all()[:3]
        context['all_stories'] = Story.objects.all()

        story_list = []
        for story in Story.objects.all():
            story_list.append(story.created_at)
        
        context['story_list'] = story_list

        form = self.form_class(self.request.GET)
        if form.is_valid():
            context['stories'] = Story.objects.filter(title__icontains=form.cleaned_data['name'])[:4]
            context['recipes'] = Recipe.objects.filter(title__icontains=form.cleaned_data['name'])[:2]
            if self.request.user.is_authenticated:
                context['user_stories'] = Story.objects.filter(user = self.request.user).filter(title__icontains=form.cleaned_data['name'])[:3]
            
        else:
            context['stories'] = Story.objects.all()[:4]
            context["recipes"] = Recipe.objects.all()[:2]
            context['user_stories'] = Story.objects.filter(user = self.request.user)[:3]
        return context
       
class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recipes"] = Recipe.objects.all()
        context['stories'] = Story.objects.all()
        context['categories'] = Category.objects.all()[:3]
        context['users'] = User.objects.all()
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
    paginate_by = 6
    queryset = Story.objects.order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.order_by('id')[:3]
       
        return context
    
    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = Story.objects.order_by('id')
            title_name = self.request.GET.get('q', None)
            if title_name is not None:
                queryset = queryset.filter(title__icontains=title_name)
            return queryset

class StoryCategoryList(ListView):
    context_object_name = 'stories'
    template_name='stories.html'
    paginate_by = 6
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()[:3]
       
        return context

    def get_queryset(self):
        self.category = get_object_or_404(Category, title=self.kwargs['category'])
        if self.request.method == 'GET':
            queryset = Story.objects.filter(category = self.category)
            title_name = self.request.GET.get('q', None)
            if title_name is not None:
                queryset = queryset.filter(title__icontains=title_name)
            return queryset
        return Story.objects.filter(category=self.category)
        

class StoryFilterView(ListView):
    model = Story
    template_name = "story-filter.html"
    context_object_name = 'stories'
    show_change_link = True
    paginate_by = 6
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.order_by('id')[:3]
       
        return context

    def get_queryset(self):
        # queryset = super().get_queryset()
        queryset = Story.objects.all()
        sort_data = self.request.GET.get('storySort')
        print(sort_data)
        if sort_data == 'newest':
            return queryset.order_by('-created_at')
        elif sort_data == 'oldest':
            return queryset.order_by('created_at')
        elif sort_data == 'famous':
            return queryset.order_by('-story_count')
        
        
        return queryset


class StoryDetail(FormMixin,DetailView):
    model = Story
    context_object_name = 'story'
    template_name='story_detail.html'
    form_class = CommentForm  
  
    def get_success_url(self):
        return reverse_lazy('stories:story_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        # post = get_object_or_404(Story, id=pk)
        # photos = StoryImage.objects.filter(story=Story.objects.filter(id = 3))
        # print(photos)
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context['stories'] = Story.objects.all()[:3]
        context['story_images'] = StoryImage.objects.all()
        context['tags']= Story.tags.most_common()
        searched_word = self.request.GET.get('q')
        if searched_word is not None:
            context['search_word'] = searched_word
        
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
        comment = form.save(commit=False)
        comment.story = get_object_or_404(Story, pk=self.kwargs.get('pk'))
        comment.save()
        return super().form_valid(form)

class RecipeList(ListView):
    model = Recipe
    context_object_name = 'recipes'
    template_name='recipes.html'
    paginate_by = 4
    queryset = Recipe.objects.order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.order_by('id')
    
        return context
    
    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = Recipe.objects.order_by('id')
            title_name = self.request.GET.get('q', None)
            if title_name is not None:
                queryset = queryset.filter(title__icontains=title_name)
            return queryset



class RecipeCategoriesList(ListView):
    context_object_name = 'recipes'
    template_name='recipes.html'  
    form_class = ProfileSearchForm
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()[:3]
        
        return context

    def get_queryset(self):
        self.category = get_object_or_404(Category, title=self.kwargs['category'])
        if self.request.method == 'GET':
            queryset = Recipe.objects.filter(category = self.category)
            title_name = self.request.GET.get('q', None)
            if title_name is not None:
                queryset = queryset.filter(title__icontains=title_name)
            return queryset
        return Recipe.objects.filter(category=self.category)
    

class RecipeFilterView(ListView):
    model = Recipe
    template_name = "recipe-filter.html"
    context_object_name = 'recipes'
    show_change_link = True
    paginate_by = 6
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.order_by('id')[:3]
       
        return context

    def get_queryset(self):
        # queryset = super().get_queryset()
        queryset = Recipe.objects.all()
        sort_data = self.request.GET.get('recipeSort')
        print(sort_data)
        if sort_data == 'newest':
            return queryset.order_by('-created_at')
        elif sort_data == 'oldest':
            return queryset.order_by('created_at')
        elif sort_data == 'famous':
            return queryset.order_by('-recipe_count')
        
        
        return queryset


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
        context['tags']= Recipe.tags.most_common()
        searched_word = self.request.GET.get('q')
        if searched_word is not None:
            context['search_word'] = searched_word
        return context

    def get_object(self):
        recipe_count = super().get_object()
        # Record the last accessed date
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
