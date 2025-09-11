from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'bancos', exchangeRateView, basename='post')
router.register(r'scrapingList', scrapingListView, basename='list')


urlpatterns = [
    path('', include(router.urls)),
    path('filtro/', exchangeRateByScrapingIDView.as_view({'get': 'list'}), name='lista-scraping-by-id'),
    path('bestPriceSell/', bestPriceSellView.as_view({'get': 'list'}), name='best-price-sell'),
    path('bestPriceBuy/', bestPriceBuyView.as_view({'get': 'list'}), name='best-price-buy'),
    path('lastScraping/', LastScrapingView.as_view({'get': 'list'}), name='last-scraping'),
]
