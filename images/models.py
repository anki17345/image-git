from django.db import models

class Image(models.Model):
    filename = models.CharField(max_length=100)
    metadata = models.TextField(null=True, blank=True)
    file = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.filename
