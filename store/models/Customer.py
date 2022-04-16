# ###
# Model classes for the Customer object
# ###

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

class Customer(models.model):
    """
    Model for Customer related details
    """

    # The owning model
    name = models.CharField(max_length=100, blank=False, null=False)
    password = models.CharField(max_length=20, blank=False)
    email = models.EmailField(max_length=100, unique=True, blank=False)

    def __str__(self):
        return self.name
    
    def normalizeEmail(self):
        return self.email.lower()

    class Meta:
        ordering = ['-id']   # i.e., newest first
