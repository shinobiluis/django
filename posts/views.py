from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# utilities
from datetime import datetime

posts = [
    {
        'name':'sadfklsdfj',
        'user':'asdfjasdflasdf',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture':'url'
    },    
    {
        'name':'sadfklsdfj',
        'user':'asdfjasdflasdf',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture':'url'
    },    
    {
        'name':'sadfklsdfj',
        'user':'asdfjasdflasdf',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture':'url'
    }    
]

def list_posts(request):
    return render(request, 'posts/feed.html', {'posts': posts})
