from django.db import models
from datetime import timedelta
class LatestCustomers(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()

class StudentDetailModel(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=None)
    father_name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name} {self.father_name}'

class StudentRecord(models.Model):
    STATUS_CHOICES = [
        ("checked_in", "Checked In"),
        ("checked_out", "Checked Out"),
        ("absent", "Absent"),
    ]
    student = models.ForeignKey(StudentDetailModel,on_delete=models.CASCADE, related_name="student_detail")
    status = models.CharField(max_length=100,choices=STATUS_CHOICES,default="absent")
    room_number = models.CharField(max_length=50)
    hostel_number = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    check_in_time = models.DateTimeField(null=True, blank=True)
    check_out_time = models.DateTimeField(null=True, blank=True)
    duration = models.DateTimeField(null=True,blank=True)
    @property
    def duration(self):
        """
         Calculate the duration the student has been checked in.
         This does NOT create a database field but allows runtime calculation.
        """
        if self.check_in_time and self.check_out_time:
            return self.check_in_time - self.check_out_time
        return timedelta(0)

    @property
    def status(self):
        """
        Determine the student's status based on check-in and check-out times.
        """
        if self.check_in_time and not self.check_out_time:
            return "Checked In"
        elif self.check_in_time and self.check_out_time:
            return "Checked Out"
        return "Absent"
    def __str__(self):
        return f"{self.student.name} - {self.status} on {self.date}"
