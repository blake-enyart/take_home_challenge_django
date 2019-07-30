from django.db import models

class Olympian(models.Model):
    GENDER = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('O', 'Other'),
    )
    MEDALS = (
        ('Bronze', 'Bronze'),
        ('Silver', 'Silver'),
        ('Gold', 'Gold'),
    )
    name = models.TextField()
    sex = models.CharField(max_length=1, choices=GENDER)
    age = models.PositiveIntegerField(null=True, blank=True)
    height = models.PositiveIntegerField(null=True, blank=True)
    weight = models.PositiveIntegerField(null=True, blank=True)
    team = models.TextField()
    games = models.TextField()
    sport = models.TextField()
    event = models.TextField()
    medal = models.CharField(max_length=15, choices=MEDALS, blank=True, null=True)
