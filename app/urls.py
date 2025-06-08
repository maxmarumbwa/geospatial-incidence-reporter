from django.urls import path
from .views import HomePageView, admin_data, incidence_data


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("incidence_data/", incidence_data, name="incidence_data"),
    path("admin_data/", admin_data, name="admin_data"),
]
