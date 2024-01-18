from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.urls import reverse
from django.template.loader import render_to_string

menu = [
    {'title': 'chiqish', 'url_name': 'about'},
    {'title': 'malumotlarni korish', 'url_name': 'addpage'},
    {'title': 'list kiritish', 'url_name': 'contact'},
    {'title': 'royxatdan otish', 'url_name': 'login'},
]
data_db = [
    {'id': 1, 'title': 'sardor shukurov', 'content': '''<h1>shukurov sardor</h1> 21.09.2003 termiz shahar. 15 maktab G sinf oquvchisi. litsey talabasi hozirda tatu talabasi''', 'is_published': True},
    {'id': 2, 'title': 'akmal omonturdiyev', 'content': 'uning yashash tarixi', 'is_published': False},
    {'id': 3, 'title': 'timur shukurov', 'content': 'uning yashash tarixi', 'is_published': True},
]


def index(request):
    # t = render_to_string('web1/index.html')
    # return HttpResponse(t)
    data = {'title': 'bosh menyu',
            'menu': menu,
            'posts': data_db
            }
    return render(request, 'web1/index.html', context=data)


def about(request):
    return render(request, 'web1/about.html', {'title': 'o list', 'menu': menu})


def show_post(request, post_id):
    return HttpResponse(f'sizga id:{post_id} ga teng bolgan listga tashrif buyurdingiz ')


def addpage(request):
    return HttpResponse('malumotlarni korish')


def contact(request):
    return HttpResponse('list kiritish')


def login(request):
    return HttpResponse('royxatdan otish')


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>list topilmadi</h1>")
