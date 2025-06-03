from django.db import models
from django.contrib.auth.models import User  # assuming owner_id references a User

class Property(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('pending', 'Pending'),
        ('occupied', 'Occupied'),
    ]

    property_types=[
        ('house','House'),
        ('apartment','Apartment'),
        ('studio','Studio'),
        ('condo','Condo'),

    ]

    property_name = models.CharField(max_length=255)
    property_description = models.TextField(blank=True)
    property_type = models.CharField(max_length=10, choices=property_types, default='house') 
    location = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    advance_amount = models.DecimalField(max_digits=10, decimal_places=2)
    current_rent = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='available')  # New field
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.CharField(max_length=255)
    eb_number = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.property_name