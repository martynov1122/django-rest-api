from django.db import models
from django.db.models import Sum

class Company(models.Model):
  name = models.CharField('Name', max_length=300)
  def __str__(self):
    return self.name
  def headquarter_address(self):
  	headquarter = self.office_set.get(headquarter=True)
  	return " ".join([headquarter.street, headquarter.postal_code, headquarter.city])
  def total_rents(self):
  	return self.office_set.aggregate(Sum('monthly_rent'))['monthly_rent__sum']

class Office(models.Model):
  company = models.ForeignKey(Company, on_delete=models.CASCADE)
  street = models.CharField('Street', max_length=256, blank=True)
  postal_code = models.CharField('Postal Code', max_length=32, blank=True)
  city = models.CharField('City', max_length=128, blank=True, null=True)
  monthly_rent = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)
  headquarter = models.BooleanField(default=False)
  def __str__(self):
    return " ".join([self.street, self.postal_code, self.city])
