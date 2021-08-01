import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE','cocktailapi.settings')

app=Celery('cocktailapi')

app.config_from_object('django.conf:settings',namespace='CELERY')

app.conf.beat_schedule ={
    'get_10lastest_cocktails_5s': {
        'task':'cocktail.tasks.get_10lastest_cocktails',
        'schedule': 5.0
    }
}

app.autodiscover_tasks()