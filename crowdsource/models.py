from django.db import models


# form data model
class CSFormData(models.Model):
    phoneno = models.IntegerField()
    waterlevel = models.FloatField()
    location = models.CharField(max_length=100 , blank=True, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name

# tweet data model
# ....