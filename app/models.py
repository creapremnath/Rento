from django.db import models
from django.conf import settings
from django.contrib.auth.models import BaseUserManager,AbstractUser,PermissionsMixin, AbstractBaseUser # assuming owner_id references a User

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
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    advance_amount = models.DecimalField(max_digits=10, decimal_places=2)
    current_rent = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='available')  # New field
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.CharField(max_length=255)
    eb_number = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.property_name
    

class UserManager(BaseUserManager):
    """Manager for Users."""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError('User must have an email address.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and return new superuser."""
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the System"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=15)
    address = models.TextField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'