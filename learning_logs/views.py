from django.shortcuts import render, redirect
from .models import Topic
from .forms import TopicForm

# Create your views here.

def index(request):
    return render(request, 'learning_logs/index.html')

def topics(request):
    topics = Topic.objects.filter(owner=request.users.order_by('date_added'))
    context = {'topics':topics}
    return render(request, 'MainApp/topics.html', context)

def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date added')
    context = {'topic':topic, 'entries':entries}

    return render(request, 'MainApp/topic.html', context)

def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(date=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('MainApp:topics')

    context = {'form':form}
    return render(request, 'MainApp/new_topic.html',context)