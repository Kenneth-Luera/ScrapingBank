from rest_framework import serializers
from .models import exchangeRate, scrapingList

class exchangeRateSerializers(serializers.ModelSerializer):
    class Meta:
        model = exchangeRate
        fields = ('__all__')
        extra_kwargs = {
            "scrapingID": {"read_only": True}
        }

class scrapingListSerializers(serializers.ModelSerializer):
    class Meta:
        model = scrapingList
        fields = ('__all__')

class filterSerializer(serializers.Serializer):
    scrapingID = serializers.UUIDField()
    class Meta:
        model=exchangeRate
        fields = ('scrapingID',)