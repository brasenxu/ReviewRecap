from django.db import models


class Product(models.Model):

    id = models.CharField(max_length=500, primary_key=True)
    last_update = models.IntegerField()

    keyword1 = models.CharField(max_length=50, default="")
    keyword1_rating = models.FloatField(default=0)
    keyword1_freq = models.IntegerField(default=0)
    keyword2 = models.CharField(max_length=50, default="")
    keyword2_rating = models.FloatField(default=0)
    keyword2_freq = models.IntegerField(default=0)
    keyword3 = models.CharField(max_length=50, default="")
    keyword3_rating = models.FloatField(default=0)
    keyword3_freq = models.IntegerField(default=0)
    keyword4 = models.CharField(max_length=50, default="")
    keyword4_rating = models.FloatField(default=0)
    keyword4_freq = models.IntegerField(default=0)
    keyword5 = models.CharField(max_length=50, default="")
    keyword5_rating = models.FloatField(default=0)
    keyword5_freq = models.IntegerField(default=0)

    def __str__(self):

        return self.id
