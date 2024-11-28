from django.http import HttpResponse, HttpRequest, HttpResponseNotFound, Http404, HttpResponseRedirect, \
    HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.template.defaultfilters import title, slugify
from django.urls import reverse
from django.template.loader import render_to_string

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'addpage'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}
        ]

data_db = [{'id': 1, 'title': 'Анджелина Джоли', 'content': 'Биография Анджелины Джоли', 'is_published': True},
           {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
           {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулии Робертс', 'is_published': True}, ]


def index(request):
    data = {'title': 'Главная страница',
            'menu': menu,
            'posts': data_db
            }
    return render(request, 'women/index.html', context=data)
    # t = render_to_string('women/index.html')
    # return HttpResponse(t)


def about(request):
    return render(request, 'women/about.html', {'title': 'О сайте'})


def show_post(request, post_id):
    return HttpResponse(f'Отоброжение стать с id = {post_id}')


def addpage(request):
    return HttpResponse(f'Добавление статьи')


def contact(request):
    return HttpResponse(f'Обратная связь')


def login(request):
    return HttpResponse(f'Авторизация')


# def categories(request, cat_id):
#     return HttpResponse(f'<h1>Статьи по категориям</h1><p>id: {cat_id}</p>')
#
#
# def categories_by_slug(request, cat_slug):
#     if request.GET:
#         print(request.GET)
#     return HttpResponse(f'<h1>Статьи по категориям</h1><p>slug: {cat_slug}</p>')
#
#
# def archive(request, year):
#     if year > 2023:
#         uri = reverse('cats_slug', args=('music',))
#         return HttpResponseRedirect(uri)
#         # return HttpResponsePermanentRedirect('/') #код 301
#         # return redirect('home') #код 302
#         # return redirect(index)
#         # return redirect(categories_by_slug, '2gfg00', permanent=True) #код 301
#         # return redirect('/')
#         # raise Http404()
#     return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')


def page_not_found(request, exception):
    return HttpResponseNotFound(f'<h1>Страница не найдена</h1>')

# Create your views here.
