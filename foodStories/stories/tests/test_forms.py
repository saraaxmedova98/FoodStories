from django.test import TestCase
from stories.models import Category
from stories.forms import StoryForm, RecipeForm, ContactForm


class StoryFormTests(TestCase):
    def test_story_forms(self):
       
        category = Category.objects.create(
            title='Category title'
            )
        valid_data = {'title': 'Story title', 'description': 'Description', 'category': category}
        form = StoryForm(data=valid_data)
        self.assertFalse(form.errors)

        invalid_data = {'title': 1,'category': category}
        form = StoryForm(data=invalid_data)
        self.assertTrue(form.errors)


class RecipeFormTests(TestCase):
    def test_story_forms(self):
       
        category = Category.objects.create(
            title='Category title'
            )
        valid_data = {'title': 'Recipe title', 'description': 'Description','ingredients':'Something', 'category': category}
        form = RecipeForm(data=valid_data)
        self.assertFalse(form.errors)

        invalid_data = {'title': 1,'category': category}
        form = RecipeForm(data=invalid_data)
        self.assertTrue(form.errors)


class ContactFormTests(TestCase):
    def test_story_forms(self):
       
        valid_data = {'name': 'Name', 'email': 'admin@gmail.com','subject':'Subject', 'message': 'message'}
        form = ContactForm(data=valid_data)
        self.assertFalse(form.errors)

        invalid_data = {'name': 'Name','email': 'admin', 'subject': "One morning Nikos woke up and walked into the bathroom. He started to shave, as he did every morning, but as he was shaving he noticed that the mirror on the bathroom wall wasn’t quite straight. He tried to move it to one side to make it straighter, but as soon as he touched it, the mirror fell off the wall and hit the floor with a huge crash. It broke into a thousand pieces. Nikos knew that some people thought this was unlucky. ‘Seven years’ bad luck,’ they said, when a mirror broke. But Nikos wasn’t superstitious. Nikos wasn’t superstitious at all. He didn’t care. He thought superstition was nonsense. He picked up the pieces of the mirror, put them in the bin and finished shaving without a mirror."}
        form = ContactForm(data=invalid_data)
        self.assertTrue(form.errors)