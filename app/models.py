from __future__ import unicode_literals
from django.contrib.gis.db import models


# Create your models here.
class Incident(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    geo_location = models.PointField(srid=4326)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class zim_adm2(models.Model):
    adm2_en = models.CharField(max_length=254)
    adm2_pcode = models.CharField(max_length=254)
    adm1_en = models.CharField(max_length=254)
    adm1_pcode = models.CharField(max_length=254)
    adm0_en = models.CharField(max_length=254)
    adm0_pcode = models.CharField(max_length=254)
    geom = models.MultiPolygonField(srid=4326)


def __str__(self):
    return self.adm2_en
