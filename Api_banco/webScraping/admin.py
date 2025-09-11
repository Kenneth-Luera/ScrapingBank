from django.contrib import admin
from .models import scrapingList, exchangeRate

class exchangeRateAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if scrapingList.objects.exists():
            form.base_fields['scrapingID'].initial = scrapingList.objects.latest('id')
        return form


admin.site.register(scrapingList)
admin.site.register(exchangeRate, exchangeRateAdmin)