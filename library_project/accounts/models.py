from django.db import models
from django.contrib.auth.models import AbstractUser

from accounts.fields import CaseInsensitiveCharField, CaseInsensitiveEmailField
from accounts.utils import validate_email_address
# Create your models here.




class CustomUser(AbstractUser):
    """
    A custom user in the Library Management System API
    The user must have a unique username which is case insensitive and a unique email
    the attributes of this model are
        username: a string field 
        email:
        bio:
        Date of membership:
        is_active:
    """

    username = CaseInsensitiveCharField(unique=True, blank=False, max_length=70, null=False)
    email = CaseInsensitiveEmailField(blank=False, null=False, unique=True)

    bio = models.TextField(max_length=500, blank=True)
    date_joined = models.DateField(verbose_name='Date of Membership', null=False, blank=False, auto_now_add=True)
    is_active = models.BooleanField(default=True)

    role_id = models.OneToOneField(to='LibraryRole', on_delete=models.CASCADE, related_name='libraryuser', null=True)
    
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


    def validate_email(self):
        """
        Validates the provided email to check if it matches a pattern and is from 
        the domain `outlook` or `gmail`
        """
        validate_email_address(self.email)
        return self.email

    class Meta:
        pass

class LibraryRole(models.Model):
    """
    Primary Library Roles
    """

    class Role(models.TextChoices):
        member = 'Member'
        librarian = 'Librarian'
        admin = 'Administrator'

    role = models.CharField(choices=Role, default='Member', max_length=20)

    def __str__(self):
        return self.role