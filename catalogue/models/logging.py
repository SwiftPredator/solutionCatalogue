from django.contrib.auth.models import User
from django.db import models


class SearchLog(models.Model):
    identifier = models.CharField("Identifier", max_length=1000)
    query = models.CharField("Anfrage", max_length=100, blank=True)
    created = models.DateTimeField("Erstellt", auto_now_add=True)

    class Meta:
        verbose_name = "Suchverlauf"
        verbose_name_plural = "Suchverläufe"

    def __str__(self):
        return "{}".format(self._meta.verbose_name)
