from rest_framework import serializers
from .models import Company, Office

class CompanyListSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Company
    fields = ('id', 'name', 'headquarter_address', 'total_rents')

class OfficeSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Office
    fields = ('id', 'street', 'postal_code', 'city', 'monthly_rent', 'headquarter')

class OfficeUpdateSerializer(serializers.HyperlinkedModelSerializer):
  headquarter = serializers.BooleanField(default=True)
  class Meta:
    model = Office
    fields = ('id', 'headquarter')

class CompanyDetailSerializer(serializers.HyperlinkedModelSerializer):
  offices = OfficeSerializer(source='office_set', many=True)
  class Meta:
    model = Company
    fields = ('id', 'name', 'offices')
