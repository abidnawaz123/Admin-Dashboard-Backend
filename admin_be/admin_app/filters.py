from django_filters import rest_framework
from .models import StudentRecord

"""
    Created this filter to filter-out the students according to the given filters. 
"""
class CustomStudentFilter(rest_framework.FilterSet):
    min_age = rest_framework.NumberFilter(field_name="student__age",lookup_expr="gte")
    max_age= rest_framework.NumberFilter(field_name="student__age",lookup_expr="lte")

    class Meta:
        model = StudentRecord
        fields = ["min_age", "max_age"]