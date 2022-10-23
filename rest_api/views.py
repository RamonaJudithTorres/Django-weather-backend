from rest_framework import viewsets
from django.http import HttpResponse
from .models import Record
from .serializers import RecordSerializer
from url_filter.integrations.drf import DjangoFilterBackend



class RecordViewSetWithOptions(viewsets.ModelViewSet):
    queryset= Record.objects.all()
    serializer_class = RecordSerializer

    filter_backends = [DjangoFilterBackend]
    filter_fields = ['city', 'date']


    # def get_queryset(self):
    #     return 

