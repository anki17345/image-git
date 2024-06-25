import django_filters
from .models import Image

class ImageFilter(django_filters.FilterSet):
    filename = django_filters.CharFilter(field_name='filename', lookup_expr='icontains')
    metadata = django_filters.CharFilter(field_name='metadata', lookup_expr='icontains')

    class Meta:
        model = Image
        fields = ['filename', 'metadata']
