from django.db import models
import uuid


def get_default_scraping():
    ultimo = scrapingList.objects.order_by('-timenow').first()
    return ultimo.id if ultimo else None


class scrapingList(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    codScraping = models.CharField(max_length=100, default="Scraping")
    timenow = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"{self.codScraping} - {self.timenow}"


class exchangeRate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    scrapingID = models.ForeignKey(
        scrapingList,
        on_delete=models.CASCADE,
        default=get_default_scraping,
        null=True,
        blank=True
    )
    name = models.CharField(max_length=100)
    compra = models.CharField(max_length=100)
    venta = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if not self.scrapingID:
            ultimo = scrapingList.objects.order_by('-timenow').first()
            if ultimo:
                self.scrapingID = ultimo
        super().save(*args, **kwargs)

    def __str__(self):
        return f"banco {self.name} con cambio compra {self.compra}, venta {self.venta}"
