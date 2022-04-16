# ###
# Model classes for the Customer object
# ###

from django.db import models

def file_upload_to(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return '{0}/{1}'.format(instance, filename)

class Books(models.model):
    """
    Model for Books related details
    """

    # The owning model
    book_name = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(null=True, blank=True)
    image_link = models.ImageField(upload_to=file_upload_to, blank=True,
                                     null=True, default=None)

    def __str__(self):
        return self.book_name

    class Meta:
        ordering = ['-id']   # i.e., newest first
