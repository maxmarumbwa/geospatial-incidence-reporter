# import layer mapping for Zimbabwe administrative boundaries
from django.contrib.gis.utils import LayerMapping
from .models import zim_adm2
import os

zim_adm2_mapping = {
    "adm2_en": "ADM2_EN",
    "adm2_pcode": "ADM2_PCODE",
    "adm1_en": "ADM1_EN",
    "adm1_pcode": "ADM1_PCODE",
    "adm0_en": "ADM0_EN",
    "adm0_pcode": "ADM0_PCODE",
    "geom": "MULTIPOLYGON",
}

admin2_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "data", "shapefile", "zim_adm2.shp")
)
# Data location /app/data/shapefile/zim_adm2.shp


def run(verbose=True):
    if verbose:
        print(f"Loading data from {admin2_shp}")
    lm = LayerMapping(
        zim_adm2,
        admin2_shp,
        zim_adm2_mapping,
        transform=False,
        encoding="utf-8",
    )
    lm.save(strict=True, verbose=verbose)
