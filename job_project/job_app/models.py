from django.contrib.auth.models import User
from django.db import models


# class Client(models.Model):
#
#     name = models.CharField(blank=False, max_length=100)
#     phone_number = models.PositiveBigIntegerField(blank=False)
#     email = models.EmailField(blank=False, primary_key=True)
#
#     def __str__(self):
#         return self.name


class Offer(models.Model):

    OFFER_CATEGORY = [('pl', 'plumbing'), ('el', 'electronics'), ('pw', 'physical work'),
                      ('cl', 'cleaning'), ('tr', 'transportation'), ('co', 'construction'),  ('ot', 'other')]

    title = models.CharField(blank=False, max_length=100)
    description = models.TextField(blank=False, max_length=500)
    category = models.CharField(blank=False, max_length=2, choices=OFFER_CATEGORY)
    payment = models.PositiveBigIntegerField(blank=False, default=0)
    city = models.CharField(blank=False, max_length=50, default="")
    issued = models.DateTimeField()
    phone = models.PositiveBigIntegerField(blank=False)
    user_id = models.CharField(blank=False, max_length=100, default="")

    def __str__(self):
        return self.title
