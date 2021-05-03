from django.shortcuts import render

from .forms import SearchForm
from .models import Package, Home, Prices


def main(request):
    packages = Package.objects.all()
    return render(request, 'index.html', {'packages': packages})


def home(request):
    main_page = Home.objects.all()
    return render(request, 'index.html', {'home': home})


def search(request):
    global results
    form = SearchForm()
    query = None
    result = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data['query']
        results = Package.objects.filter(name__startswith=query)
    return render(request, 'search.html', {'form': form, 'query': query, 'results': results})


def prices(request):
    check_prices = Prices.objects.all()
    return render(request, 'base.html', {'prices': prices})

