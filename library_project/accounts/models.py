from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    """
    This is a custom user model which will be used in the Library Management API
    """

    bio = models.TextField(max_length=500, blank=True)
    email = models.EmailField(blank=False, null=False)
    
    def __str__(self):
        """
        Returns the username of the user
        """
        return self.username
    
    def get_absolute_url(self):
        """
        to be implemented later
        """
        pass

