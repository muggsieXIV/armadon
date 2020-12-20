from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('amadon', views.amadon),
    path('amadon/{{product_id}}/checkout', views.checkout),
    path('amadon/process_product', views.process_product),
]

