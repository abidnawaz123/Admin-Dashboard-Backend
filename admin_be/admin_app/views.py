from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from rest_framework.permissions import IsAuthenticated

class LatestCustomersView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = LatestCustomers.objects.all()
    serializer_class = LatestCustomersSerializer
