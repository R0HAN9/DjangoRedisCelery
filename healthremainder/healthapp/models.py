from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)  # future email/phone

    def __str__(self):
        return self.name

class Reminder(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medicine_name = models.CharField(max_length=100)
    time = models.TimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.medicine_name} for {self.patient.name} at {self.time}"
