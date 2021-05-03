from .views import main, home, search, prices
from django.urls import path

urlpatterns = [
    path('', main, name='main'),
    path('', home, name='home'),
    path('/search', search, name='search'),
    path('/prices', prices, name='prices'),
]