from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from rest_framework.permissions import IsAuthenticated,AllowAny

class LatestCustomersView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = LatestCustomers.objects.all()
    serializer_class = LatestCustomersSerializer

class StudentRecordView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = StudentRecord.objects.all()
    serializer_class = StudentRecordSerializer