# ###
# FavouriteBooks Model classes 
# ###

from django.db import models

class FavouriteBooks(models.Model):
    """
    Model for FavouriteBooks related details
    """

    # The owning model
    customer_id = models.ForeignKey('Customer', null=False, on_delete=models.CASCADE)
    favourite_books_list = models.ManyToManyField('Books')

    def __str__(self):
        favourite_books_list  = ','.join(str(v) for v in self.favourite_books_list.all())
        return favourite_books_list

    class Meta:
        verbose_name_plural = 'Favourite Books'
        ordering = ['-id']   # i.e., newest first
