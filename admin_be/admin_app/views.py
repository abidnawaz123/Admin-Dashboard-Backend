from django.shortcuts import render
from rest_framework import generics
from .serializers import *

class LatestCustomersView(generics.ListAPIView):
    queryset = LatestCustomers.objects.all()
    serializer_class = LatestCustomersSerializer


