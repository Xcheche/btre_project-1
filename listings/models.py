from django.db import models
from datetime import datetime
from realtors.models import Realtor

from ckeditor.fields import RichTextField

from cloudinary.models import CloudinaryField

class Listing(models.Model):
  realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
  title = models.CharField(max_length=200)
  address = models.CharField(max_length=200)
  city = models.CharField(max_length=100)
  state = models.CharField(max_length=100)
  zipcode = models.CharField(max_length=20)
  description = RichTextField(blank=True)
  price = models.IntegerField()
  bedrooms = models.IntegerField()
  bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
  garage = models.IntegerField(default=0)
  sqft = models.IntegerField()
  lot_size = models.DecimalField(max_digits=5, decimal_places=1)
  photo_main = CloudinaryField('image', folder='listings/images/photo_main')
  photo_1 = CloudinaryField('image', folder='listings/images/photo_1', blank=True)
  photo_2 = CloudinaryField('image', folder='listings/images/photo_2', blank=True)
  photo_3 = CloudinaryField('image', folder='listings/images/photo_3', blank=True)
  photo_4 = CloudinaryField('image', folder='listings/images/photo_4', blank=True)
  photo_5 = CloudinaryField('image', folder='listings/images/photo_5', blank=True)
  photo_6 = CloudinaryField('image', folder='listings/images/photo_6', blank=True)
  is_published = models.BooleanField(default=True)
  list_date = models.DateTimeField(default=datetime.now, blank=True)

  def __str__(self):
    return f'{self.title} - {self.id}'