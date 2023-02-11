from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255, default=None, null=True)
    no_of_guest = models.IntegerField(default=None, null=True)
    BookingDate = models.DateTimeField()
    
    def __str__(self) -> str:
        return self.name
    
class Menu(models.Model):
    title = models.CharField(max_length=255, default=None, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=None, null=True)
    inventory = models.IntegerField(default=None, null=True)
    
    def __str__(self) -> str:
        return self.title