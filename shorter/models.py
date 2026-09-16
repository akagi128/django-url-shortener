from django.db import models

# Create your models here.
class ShortURL(models.Model):
    origUrl = models.CharField(max_length = 20)
    shortcode = models.CharField(max_length = 10)
