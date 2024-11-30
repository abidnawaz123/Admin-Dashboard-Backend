from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework import filters
from .filters import CustomStudentFilter
from django_filters.rest_framework import DjangoFilterBackend

class LatestCustomersView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = LatestCustomers.objects.all()
    serializer_class = LatestCustomersSerializer

class StudentRecordView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = StudentRecord.objects.all()
    serializer_class = StudentRecordSerializer
    """This field below helps me filter using query like '?search=name OR age' """
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend
        ]
    filterset_class = CustomStudentFilter 
    search_fields = ['student__name','student__age']
    ordering_fields = ['student__name','student__age']

class HostelView(generics.ListAPIView):
    queryset = HostelView.objects.all()
    serializer_class = HostelSerializer