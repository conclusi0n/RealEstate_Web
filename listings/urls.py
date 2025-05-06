from django.urls import path
from . import views

urlpatterns = [
    path('', views.listing_view, name='listings'),
    path('listing/<int:pk>/', views.listing_detail, name='listing_detail'),
    path('rent/', views.rent_listings, name='rent_listings'),
    path('rent/<int:pk>/', views.rent_listing_detail, name='rent_listing_detail'),
]