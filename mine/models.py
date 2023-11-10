from django.db import models

class Ranking(models.Model):
    name = models.CharField(max_length=255)
    elapsed_time = models.TimeField()