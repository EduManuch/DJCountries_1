from django.shortcuts import render
from django.http import HttpResponseNotFound
import json

with open('countries.json', 'r') as f:
    c_data = json.load(f)


def home(request):
    context = {'greeting': 'Hello world !'}
    return render(request, 'index.html', context)


def countries_list(request):
    context = {'c_list': c_data}
    return render(request, 'countries-list.html', context)


def country_page(request, country):
    for data in c_data:
        if data['country'] == country:
            context = {'data': data}
            return render(request, 'country-page.html', context)
    return HttpResponseNotFound(f'Страна {country} не найдена')