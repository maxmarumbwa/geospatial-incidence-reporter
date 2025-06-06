from django.contrib import admin
from .models import Incident

# Register your models here.
# admin.site.register(Incident)


class IncidentAdmin(admin.ModelAdmin):
    list_display = ("name", "location", "created_at")


admin.site.register(Incident, IncidentAdmin)
