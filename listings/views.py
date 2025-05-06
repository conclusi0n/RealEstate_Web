from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.db.models import Q

def listing_view(request):
    query = request.GET.get('q', '')
    property_type = request.GET.get('type', '')
    city = request.GET.get('city', '')
    min_price = request.GET.get('min_price', '')
    max_price = request.GET.get('max_price', '')
    sort = request.GET.get('sort', 'price')
    purpose = request.GET.get('purpose', '')
    id = request.GET.get('id', '')

    listings = Listing.objects.all()

    if id:
        # Remove ERN- prefix if present
        id_val = id.replace('ERN-', '').strip()
        if id_val.isdigit():
            listings = listings.filter(id=int(id_val))
        else:
            listings = listings.none()
    if query:
        listings = listings.filter(title__icontains=query)
    if property_type:
        listings = listings.filter(property_type__name__iexact=property_type)
    if city:
        listings = listings.filter(city__name__iexact=city)
    if min_price:
        listings = listings.filter(price__gte=min_price)
    if max_price:
        listings = listings.filter(price__lte=max_price)
    if purpose:
        listings = listings.filter(purpose=purpose)

    if sort == 'name':
        listings = listings.order_by('title')
    elif sort == 'type':
        listings = listings.order_by('property_type__name')
    elif sort == 'city':
        listings = listings.order_by('city__name')
    elif sort == 'price_desc':
        listings = listings.order_by('-price')
    else:
        listings = listings.order_by('price')

    all_types = Listing.objects.values_list('property_type__name', flat=True).distinct()
    all_cities = Listing.objects.values_list('city__name', flat=True).distinct()

    return render(request, 'listings/listings.html', {
        'listings': listings,
        'query': query,
        'property_type': property_type,
        'city': city,
        'min_price': min_price,
        'max_price': max_price,
        'sort': sort,
        'all_types': all_types,
        'all_cities': all_cities,
        'purpose': purpose,
        'id': id,
    })


def listing_detail(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    return render(request, 'listings/listing_detail.html', {'listing': listing})


def rent_listings(request):
    query = request.GET.get('q', '')
    property_type = request.GET.get('type', '')
    city = request.GET.get('city', '')
    min_price = request.GET.get('min_price', '')
    max_price = request.GET.get('max_price', '')
    sort = request.GET.get('sort', 'price')

    listings = Listing.objects.filter(purpose='Rent')

    if query:
        listings = listings.filter(title__icontains=query)
    if property_type:
        listings = listings.filter(property_type__iexact=property_type)
    if city:
        listings = listings.filter(city__name__iexact=city)
    if min_price:
        listings = listings.filter(price__gte=min_price)
    if max_price:
        listings = listings.filter(price__lte=max_price)

    if sort == 'name':
        listings = listings.order_by('title')
    elif sort == 'type':
        listings = listings.order_by('property_type')
    elif sort == 'city':
        listings = listings.order_by('city__name')
    elif sort == 'price_desc':
        listings = listings.order_by('-price')
    else:
        listings = listings.order_by('price')

    all_types = Listing.objects.filter(purpose='Rent').values_list('property_type', flat=True).distinct()
    all_cities = Listing.objects.filter(purpose='Rent').values_list('city__name', flat=True).distinct()

    return render(request, 'listings/rent_listings.html', {
        'listings': listings,
        'query': query,
        'property_type': property_type,
        'city': city,
        'min_price': min_price,
        'max_price': max_price,
        'sort': sort,
        'all_types': all_types,
        'all_cities': all_cities,
    })


def rent_listing_detail(request, pk):
    listing = get_object_or_404(Listing, pk=pk, purpose='Rent')
    return render(request, 'listings/rent_listing_detail.html', {'listing': listing})
