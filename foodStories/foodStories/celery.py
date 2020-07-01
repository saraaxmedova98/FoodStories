from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'foodStories.settings')

app = Celery('foodStories')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'add-every-15-seconds': {
        'task': 'stories.tasks.subscribers_email',
        'schedule': crontab(minute=0, hour=0)
    },
     'add-every-30-seconds': {
        'task': 'stories.tasks.export_users_xls',
        'schedule': crontab()
    },
}
app.conf.timezone = 'UTC'



# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))