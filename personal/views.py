from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'personal/home.html')


def contact(request):
    return render(request,
                  'personal/basic.html',
                  {'content': ['My contact eMail:',
                               'example@mail.com']})
