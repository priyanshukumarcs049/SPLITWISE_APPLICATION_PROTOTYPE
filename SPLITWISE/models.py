from django.db import models
from django.db.models.functions import Cast
from django.db.models import FloatField

class ACTIVITY(models.Model):
    Who_has_paid = models.CharField(max_length=250)
    Amount_person_has_paid = models.IntegerField()
    Items_on_which_spent = models.CharField(max_length=250)
    Split_between_number_of_people = models.IntegerField()

class PEOPLE(models.Model):
    add_person = models.IntegerField()
    who_are_you_with = models.CharField(max_length=500)    

class CALCULATION(models.Model):
    Amount_paid_by_one_person = models.IntegerField()
    Number_of_People_in_group = models.IntegerField()
    Total_amount_spent_by_one_person = models.IntegerField()