from django.shortcuts import render
from .models import Topic, Topics

# Create your views here.

def index(request):
    return render(request, 'learning_logs/index.html')

def topics(request):
    topics = Topic.objects.filter(owner=request.users.order_by('date_added'))
    context = {'topics':topics}
    return render(request, 'MainApp/topics.html', context)

def topic(request, topic_id):
    topic = Topics.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date added')
    context = {'topic':topic, 'entries':entries}

    return render(request, 'MainApp/topic.html', context)