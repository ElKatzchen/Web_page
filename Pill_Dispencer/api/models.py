from django.db import models

class User(models.Model):
    Name = models.CharField(max_length=255)
    Age = models.PositiveIntegerField()
    CI = models.CharField(max_length=15, primary_key=True)

    def __str__(self):
        return f"{self.Name} with CI: {self.CI}"

class MedicineSchedule(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE, related_name="schedules")
    
    MedicineName = models.CharField(max_length=255)
    Dose = models.CharField(max_length=100)
    Description = models.TextField(blank=True, null=True)

    Day = models.CharField(max_length=20, choices=[
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
        ('All Days', 'All Days'),
    ])
    Hour = models.TimeField()

    def __str__(self):
        return f"{self.MedicineName} for {self.User.Name} on {self.Day} at {self.Hour}"
