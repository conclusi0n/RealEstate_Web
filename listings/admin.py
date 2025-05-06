from django.contrib import admin
from .models import Home, Facility, Image, City, PropertyType
from django.utils.html import format_html

class FacilityInline(admin.TabularInline):
    model = Facility
    extra = 1

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    inlines = [FacilityInline, ImageInline]
    list_display = ('title', 'city', 'area', 'price', 'price_text', 'purpose', 'property_type', 'property_face', 'bedrooms', 'bathrooms', 'toilets', 'floors', 'featured', 'date_posted')
    search_fields = ('title', 'city__name', 'area', 'municipality')
    list_filter = ('purpose', 'city', 'property_type', 'featured')
    # property_face is now editable

@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ('name', 'distance', 'home')
    search_fields = ('name', 'home__title')

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('home', 'image', 'image_tag')
    search_fields = ('home__title',)
    readonly_fields = ('image_tag',)

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" />', obj.image.url)
        return "No Image"
    image_tag.short_description = 'Preview'

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(PropertyType)
class PropertyTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
