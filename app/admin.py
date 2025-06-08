from django.contrib import admin
from .models import Incident, zim_adm2
from leaflet.admin import LeafletGeoAdmin


# version with LeafletGeoAdmin for better map integration
class IncidentAdmin(LeafletGeoAdmin):
    list_display = ("name", "location", "geo_location", "created_at")
    search_fields = ("adm2_en", "location")
    list_filter = ("created_at",)


class zim_adm2Admin(LeafletGeoAdmin):
    list_display = (
        "adm2_en",
        "adm2_pcode",
        "adm1_en",
        "adm1_pcode",
        "adm0_en",
        "adm0_pcode",
    )
    search_fields = ("adm2_en", "adm1_en", "adm0_en")
    list_filter = ("adm1_en",)


admin.site.register(Incident, IncidentAdmin)
admin.site.register(zim_adm2, LeafletGeoAdmin)
