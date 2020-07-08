from django.test import TestCase, Client
from django.urls import reverse
from stories.models import Contact, Story


class HomeViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    
    def test_home_view(self):
        url = reverse("stories:about")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, template_name='about.html')



# class StoryViewTest(TestCase):
#     def setUp(self):
#         self.client = Client()

    
#     def test_story_view(self):
#         url = reverse("stories:stories")
#         resp = self.client.get(url)

#         self.assertEqual(resp.status_code, 200)

#         self.assertTemplateUsed(resp, template_name='stories.html')


class RecipeViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    
    def test_story_view(self):
        url = reverse("stories:recipes")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, template_name='recipes.html')


class ContactViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    
    def test_story_view(self):
        url = reverse("stories:contact")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, template_name='contact.html')

        contact = Contact.objects.last()
        print(contact)
        
        request_data = {
            'name': 'Your Name',
            'email': 'admin@gmail.com',
            'subject': 'your subject',
            'message': 'message'
        }

        response = self.client.post(url , request_data)

        self.assertEqual(response.status_code, 302)


class LoginViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    
    def test_story_view(self):
        url = reverse("account:login")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, template_name='registration/login.html')


# class StoryDetailViewTest(TestCase):
    
#     def setUp(self):
#         self.story = Story.objects.create(
#             title='Story title',
#             description='Description',
#             story_image = 'stories/', 
#             )

#         self.url = reverse("stories:story_detail", kwargs={'pk': self.story.pk})
#         self.resp = self.client.get(self.url)
        
#     def test_story_view(self):
        
        

#         # self.assertEqual(resp.status_code, 200)

#         self.assertTemplateUsed(self.resp, template_name='story_detail.html')



class UserProfileViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    
    def test_home_view(self):
        url = reverse("stories:about")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, template_name='about.html')

