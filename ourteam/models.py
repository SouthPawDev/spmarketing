from django.db import models
from django.urls import reverse
# Create your models here.


class Franchises(models.Model):
    name = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
    phone_number = models.CharField(max_length=12)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ourteam", kwargs={'pk': self.pk})


class Cars(models.Model):
    brand = models.CharField(max_length=256)
    car_model = models.CharField(max_length=256)
    car_number = models.IntegerField()

    def __str__(self):
        return self.car_model, self.car_number


class Smr(models.Model):
    smr_pic = models.ImageField(upload_to='smr_pics')
    name = models.CharField(max_length=256)
    territory = models.CharField(max_length=256)
    car = models.ForeignKey(Cars, related_name='smrs', on_delete='PROTECT')
    franchise = models.ForeignKey(Franchises, related_name='smrs', on_delete='PROTECT')

    def __str__(self):
        return self.name
