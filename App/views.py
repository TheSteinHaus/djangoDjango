from django.shortcuts import render
from .models import Post

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    },
    {
        'author': 'ЗагумЁннов',
        'title': 'И где все!?',
        'content': '†††††††††††††† Стас умер ††††††††††††††',
        'date_posted': 'Now'
    }
]


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'app/home.html', context)


def about(request):
    return render(request, 'app/about.html', {'title': 'About'})


def map(request):
    return render(request, 'app/map.html', {'title': 'Map'})
