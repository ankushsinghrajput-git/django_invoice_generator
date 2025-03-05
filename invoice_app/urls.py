from django.urls import path
from .views import generate_pdf

urlpatterns = [
    path("generate-invoice/", generate_pdf, name="generate_invoice"),
]
