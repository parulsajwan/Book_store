# ###
# Model classes for the Customer object
# ###

from django.db import models
class Books(models.Model):
    """
    Model for Books related details
    """

    # The owning model
    book_name = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(null=True, blank=True)
    image_link = models.ImageField( blank=True, null=True)

    def __str__(self):
        return self.book_name
    class Meta:
        verbose_name_plural = 'Books'
        ordering = ['-id']   # i.e., newest first
