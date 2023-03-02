from django.db import models
from django.utils import timezone
# Create your models here.

class Counties(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Sub_counties(models.Model):
    name =models.CharField(max_length=50)
    county = models.ForeignKey(Counties,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Wards(models.Model):
    name = models.CharField(max_length=50)
    Sub_county = models.ForeignKey(Sub_counties,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    

class Hospital(models.Model):
    name = models.CharField(max_length=60)
    sub_county = models.ForeignKey(Sub_counties,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Ambulance(models.Model):
    no_plate = models.CharField(max_length=50)
    body = models.CharField( max_length=50)
    hospital = models.ForeignKey(Hospital,on_delete=models.CASCADE)
    requested =models.BooleanField(default=False)

    def request(self):
        self.requested = True
        self.save()

    def __str__(self):
        return self.body
    