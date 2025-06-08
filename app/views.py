from django.shortcuts import render
from django.views.generic import TemplateView
from .models import zim_adm2, Incident
from django.core.serializers import serialize
from django.http import HttpResponse


class HomePageView(TemplateView):
    template_name = "home.html"


def admin_data(request):
    admin_data = serialize("geojson", zim_adm2.objects.all())
    return HttpResponse(admin_data, content_type="json")


def incidence_data(request):
    incident_data = serialize("geojson", Incident.objects.all())
    return HttpResponse(incident_data, content_type="json")
