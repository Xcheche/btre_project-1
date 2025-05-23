from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

from cloudinary.models import CloudinaryField

class Realtor(models.Model):
  name = models.CharField(max_length=200)
  photo = CloudinaryField('image', folder='realtors/images')
  description = RichTextField(blank=True)
  phone = models.CharField(max_length=20)
  email = models.CharField(max_length=50)
  is_mvp = models.BooleanField(default=False)
  hire_date = models.DateTimeField(default=datetime.now, blank=True)
  
  def __str__(self):
    return self.name