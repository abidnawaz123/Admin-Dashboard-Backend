from .models import *
from rest_framework import serializers
class LatestCustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = LatestCustomers
        fields = '__all__'

class StudentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDetailModel
        fields = ['name','age','father_name']
        

class StudentRecordSerializer(serializers.ModelSerializer):
    student = StudentDetailSerializer()
    class Meta:
        model = StudentRecord
        fields = ["status","room_number","hostel_number","date","duration","check_in_time","check_out_time","student"]
        
class FurnitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Furniture
        fields = ["ceiling_fan","table","chair","refrigerator"]

class HostelSerializer(serializers.ModelSerializer):
    furniture = FurnitureSerializer()
    class Meta:
        model = HostelView
        fields = ["name","rooms","occupied","floors","furniture","location"]
