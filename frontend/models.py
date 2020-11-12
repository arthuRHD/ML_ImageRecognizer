from django.db import models
from datetime import datetime


class Image(models.Model):
    file = models.ImageField(upload_to='images', default=None)
    upload_date = models.DateTimeField(default=datetime.now())
    size = models.BigIntegerField()
    accuracy = models.FloatField()
    class_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.file}_{self.upload_date}"