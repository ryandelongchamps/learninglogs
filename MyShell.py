import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learning_log.settings')

import django
django.setup()

from learning_logs.models import Topic

topics = Topic.objects.all()

for topic in topics:
    print(topic.id, topic)

from django.contrib.auth.models import User

for user in User.objects.all():
    print(user.username, user.id)