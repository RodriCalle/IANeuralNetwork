from django.db import models

# Create your models here.

class ImgUpload(models.Model):
    file = models.ImageField(upload_to='imagenes', null=False)