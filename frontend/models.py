from django.db import models
from datetime import datetime


class Image(models.Model):
    file = models.ImageField(upload_to='images', default=None)
    upload_date = models.DateTimeField(default=datetime.now())
