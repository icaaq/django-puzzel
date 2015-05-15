from django.db import models


class Level(models.Model):
    level_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Bit(models.Model):
    level = models.ForeignKey(Level)
    bit_text = models.CharField(max_length=200)