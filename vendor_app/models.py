from django.db import models


# Create your models here.
class Vendor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_no = models.BigIntegerField()

    def __str__(self):
        return self.name


class VendorAddress(models.Model):
    vendor_id = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    vendor_addr = models.TextField(max_length=200)
