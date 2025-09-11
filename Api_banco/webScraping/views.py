from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import exchangeRate, scrapingList
from .serializers import exchangeRateSerializers, scrapingListSerializers, filterSerializer

class exchangeRateView(viewsets.ModelViewSet):
    serializer_class = exchangeRateSerializers
    queryset = exchangeRate.objects.all()
    permission_classes = [AllowAny] 

class scrapingListView(viewsets.ModelViewSet):
    serializer_class = scrapingListSerializers
    queryset = scrapingList.objects.all()
    permission_classes = [AllowAny]

class exchangeRateByScrapingIDView(viewsets.ViewSet):
    serializer_class = filterSerializer
    queryset = exchangeRate.objects.all().order_by('-scrapingID__timenow')
    permission_classes = [AllowAny]

    def list(self, request, scrapingID=None):
        mi_queryset = self.queryset
        ultimo_objeto = mi_queryset[0]
        default_scrapingID = ultimo_objeto.scrapingID.id
        if default_scrapingID is not None:
            exchange_rates = exchangeRate.objects.filter(scrapingID=default_scrapingID)
            serializer = exchangeRateSerializers(exchange_rates, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"detail": "scrapingID parameter is required."}, status=status.HTTP_400_BAD_REQUEST)

class LastScrapingView(viewsets.ViewSet):
    serializer_class = scrapingListSerializers
    queryset = scrapingList.objects.all().order_by('-timenow')
    permission_classes = [AllowAny]
    http_method_names = ['get']

    def list(self, request):
        ultimo = self.queryset.first()
        if ultimo:
            serializer = scrapingListSerializers(ultimo)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"detail": "No scraping records found."}, status=status.HTTP_404_NOT_FOUND)

class bestPriceSellView(viewsets.ViewSet):
    serializer_class = filterSerializer
    queryset = exchangeRate.objects.all().order_by('-scrapingID__timenow')
    permission_classes = [AllowAny]
    http_method_names = ['get']

    def list(self, request):
        resultado = exchangeRate.objects.order_by('compra').first()
        serializer = exchangeRateSerializers(resultado)
        return Response(serializer.data, status=status.HTTP_200_OK)

class bestPriceBuyView(viewsets.ViewSet):
    serializer_class = filterSerializer
    queryset = exchangeRate.objects.all().order_by('-scrapingID__timenow')
    permission_classes = [AllowAny]
    http_method_names = ['get']

    def list(self, request):
        resultado = exchangeRate.objects.order_by('-venta').first()
        serializer = exchangeRateSerializers(resultado)
        return Response(serializer.data, status=status.HTTP_200_OK)