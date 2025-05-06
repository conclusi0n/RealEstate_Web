from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class PropertyType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class Home(models.Model):
    PURPOSE_CHOICES = [
        ('Sell', 'Sell'),
        ('Rent', 'Rent'),
    ]
    FACE_CHOICES = [
        ('East', 'East'),
        ('West', 'West'),
        ('North', 'North'),
        ('South', 'South'),
        ('North-East', 'North-East'),
        ('North-West', 'North-West'),
        ('South-East', 'South-East'),
        ('South-West', 'South-West'),
    ]
    title = models.CharField(max_length=255)  # e.g. "Residential House for Sale"
    property_type = models.ForeignKey(PropertyType, on_delete=models.SET_NULL, null=True, blank=True)
    property_face = models.CharField(max_length=50, choices=FACE_CHOICES, default='East')
    year_built = models.CharField(max_length=10)
    road_type = models.CharField(max_length=50)
    negotiable = models.BooleanField(default=False)
    furnishing = models.CharField(max_length=50)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)
    area = models.CharField(max_length=100)
    price_text = models.CharField(max_length=100)  # "3 Crore 95 Lakh"
    purpose = models.CharField(max_length=10, choices=PURPOSE_CHOICES, default='Sell')
    property_area = models.CharField(max_length=50)  # e.g. "4 Aana"
    built_up_area = models.CharField(max_length=100)
    road_access = models.CharField(max_length=50)
    dimension = models.CharField(max_length=50)  # e.g. "F 30 Feet"
    date_posted = models.DateField()
    municipality = models.CharField(max_length=100)
    ward_no = models.CharField(max_length=10)
    ring_road_distance = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    bedrooms = models.IntegerField(null=True, blank=True)
    bathrooms = models.IntegerField(null=True, blank=True)
    toilets = models.IntegerField(null=True, blank=True)
    floors = models.IntegerField(null=True, blank=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Facility(models.Model):
    home = models.ForeignKey(Home, related_name='facilities', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    distance = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} - {self.distance}"

class Image(models.Model):
    home = models.ForeignKey(Home, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='home_images/')

    def __str__(self):
        return f"Image for {self.home.title}"

# Alias for backward compatibility
Listing = Home
