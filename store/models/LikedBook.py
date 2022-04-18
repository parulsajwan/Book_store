# ###
# Model classes for the BookLiked
# ###

from enum import unique
from django.db import models

class LikedBook(models.Model):
    """
    Model for LikedBook related details
    """

    # The owning model
    customer_id = models.ForeignKey('Customer', null=False, on_delete=models.CASCADE)
    liked = models.ForeignKey('Books', null=False, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.liked)

    class Meta:
        ordering = ['-id']   # i.e., newest first
        unique_together = ('customer_id','liked')
