from django.shortcuts import render

info = [
    {
        'name': 'Stas',
        'age': 23,
        'content': 'My little site',
        'date_posted': '02.12.2021'
    }

]


def home(request):
    return render(request, 'my_site/home_page.html', {'title': 'Home Page'})


def about_author(request):
    post = {'info': info}
    return render(request, 'my_site/about.html', post)
