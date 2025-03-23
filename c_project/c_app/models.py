from django.db import models
from django.db import models
class Carousel(models.Model):
    title = models.CharField(max_length=255, blank=True,null=True)
    image = models.ImageField(upload_to='carousel_images/')
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
def __str__(self):
    return self.title if self.title else "Carousel Image"