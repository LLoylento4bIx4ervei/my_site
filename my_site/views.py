from django.shortcuts import render
from .models import Post
from django.contrib.auth.models import User

info = [
    {
        'name': 'Stas',
        'age': 23,
        'content': 'My little site',
        'date_posted': '02.12.2021'
    }

]


def home(request):
    post = {'info': Post.objects.all()}
    return render(request, 'my_site/home_page.html', post)


def about_author(request):

    return render(request, 'my_site/about.html')
