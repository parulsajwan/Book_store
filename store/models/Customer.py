# ###
# Model classes for the Customer object
# ###

from django.db import models
class Customer(models.Model):
    """
    Model for Customer related details
    """

    # The owning model
    name = models.CharField(max_length=100, blank=False, null=False)
    password = models.CharField(max_length=128, blank=False, null=False)
    email = models.EmailField(max_length=100, unique=True, blank=False)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        return super(Customer, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ['-id']   # i.e., newest first
