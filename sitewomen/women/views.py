from django.http import HttpResponse, HttpRequest, HttpResponseNotFound, Http404, HttpResponseRedirect, \
    HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return HttpResponse('Страница приложения women.')


def categories(request, cat_id):
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>id: {cat_id}</p>')


def categories_by_slug(request, cat_slug):
    if request.GET:
        print(request.GET)
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>slug: {cat_slug}</p>')


def archive(request, year):
    if year > 2023:
        uri = reverse('cats_slug', args=('music',) )
        return HttpResponseRedirect(uri)
        # return HttpResponsePermanentRedirect('/') #код 301
        # return redirect('home') #код 302
        # return redirect(index)
        # return redirect(categories_by_slug, '2gfg00', permanent=True) #код 301
        # return redirect('/')
        # raise Http404()
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')


def page_not_found(request, exception):
    return HttpResponseNotFound(f'<h1>Страница не найдена</h1>')

# Create your views here.
