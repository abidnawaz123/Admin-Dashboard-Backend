from django.db import models
from datetime import timedelta
class LatestCustomers(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

class StudentDetailModel(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=None)
    father_name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name} {self.father_name}'

class Furniture(models.Model):
    ceiling_fan = models.IntegerField(default=0)
    table = models.IntegerField(default=0)
    chair = models.IntegerField(default=0)
    refrigerator = models.IntegerField(default=0)
    def __str__(self):
        return f'Furniture : {self.id}'

class HostelView(models.Model):
    name = models.CharField(max_length=200)
    rooms = models.IntegerField(default=None)
    occupied = models.IntegerField(default=0)
    floors = models.IntegerField(default=None)
    location = models.CharField(max_length=300,null=True,blank=True)
    furniture = models.ForeignKey(Furniture, on_delete=models.CASCADE) 
    
    def __str__(self):
        return f'{self.name}'   
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
    duration = models.DurationField(null=True, blank=True)  # Use DurationField to store the time difference
    def save(self, *args, **kwargs):
            if self.check_in_time and not self.check_out_time:
                self.status = "checked_in"
            elif self.check_out_time:
                self.status = "checked_out"
                # Calculate the duration only when check_out_time is set
                if self.check_in_time:
                    self.duration = self.check_out_time - self.check_in_time

            super().save(*args, **kwargs)

    @property
    def formatted_duration(self):
        """
        Returns a human-readable duration, in hours, minutes, and seconds.
        """
        if self.duration:
            total_seconds = self.duration.total_seconds()
            hours, remainder = divmod(total_seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            return f"{int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds"
        return "0 hours, 0 minutes, 0 seconds"

    def __str__(self):
        return f"{self.student.name} - {self.status} on {self.date}"
    @property
    def duration(self):
        """
        Calculate the duration between check-in and check-out times in a human-readable format.
        """
        if self.check_in_time and self.check_out_time:
            delta = self.check_out_time - self.check_in_time
            total_seconds = int(delta.total_seconds())
            hours, remainder = divmod(total_seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            return f"{hours}h {minutes}m {seconds}s"
        return "0h 0m 0s"

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
