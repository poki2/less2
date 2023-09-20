import requests
from django.shortcuts import render

# Create your views here.
from app4.models import Foo


def foo(request):
    data = requests.get('https://jsonplaceholder.typicode.com/todos')
    if not list(Foo.objects.all()):
        for user in data.json():
            Foo.objects.create(
                userId=user.get('userId'),
                _id=user.get('id'),
                title=user.get('title'),
                completed=user.get('completed')
            )
        print('empty')
    else:
        print('not empty')
    context = {'data': data.json()}

    return render(request, 'index.html', context)