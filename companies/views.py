from rest_framework import viewsets, generics, mixins
from .models import Company, Office
from companies.serializers import CompanyListSerializer, CompanyDetailSerializer, OfficeSerializer, OfficeUpdateSerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response

class CompanyViewSet(mixins.ListModelMixin, GenericViewSet):
  queryset = Company.objects.all()
  serializer_class = CompanyListSerializer

class CompanyDetailViewSet(mixins.RetrieveModelMixin, GenericViewSet):
  queryset = Company.objects.all()
  serializer_class = CompanyDetailSerializer

class OfficeUpdateView(mixins.UpdateModelMixin, GenericViewSet):
  queryset = Office.objects.all()
  serializer_class = OfficeUpdateSerializer
  def update(self, request, *args, **kwargs):
    partial = kwargs.pop('partial', False)
    instance = self.get_object()
    ### Remove old headquarter #####
    office = Office.objects.get(pk=self.kwargs.get('pk'))
    headquarter_office = office.company.office_set.filter(headquarter=True).first()    
    headquarter_office.headquarter = False
    headquarter_office.save()
    ################################
    serializer = self.get_serializer(instance, data=request.data, partial=partial)
    serializer.is_valid(raise_exception=True)
    self.perform_update(serializer)

    if getattr(instance, '_prefetched_objects_cache', None):
        # If 'prefetch_related' has been applied to a queryset, we need to
        # forcibly invalidate the prefetch cache on the instance.
        instance._prefetched_objects_cache = {}

    return Response(serializer.data)