from django.db import models

# Create your models here.


class Rayyith(models.Model):
    id_number = models.CharField("ID Card Number", max_length=10, unique=True)
    name = models.CharField("Rayyith Name",  max_length=64)
    address = models.CharField("Address", max_length=256)
    dob = models.DateField("Date of Birth")


class ScheduleItem(models.Model):
    name = models.CharField("Schedule Name",  max_length=64)
    due_on = models.IntegerField("Schedule Item Due (in weeks)")

    def __str__(self):
        return self.name


class Vaccination(models.Model):
    rayyith = models.ForeignKey('Rayyith', on_delete=models.PROTECT)
    schedule_item = models.ForeignKey('ScheduleItem', on_delete=models.PROTECT)
    date_on = models.DateTimeField("Date Administered")
