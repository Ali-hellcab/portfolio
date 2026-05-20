from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path("",                        views.index,          name="index"),
    path("project/<slug:slug>/",    views.project_detail, name="project_detail"),
    path("contact/",                views.contact,        name="contact"),
]
