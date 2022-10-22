from django.db import models


class NIDInfo(models.Model):
    nid_number = models.CharField(max_length=50)
    contact_number = models.IntegerField()

    def __str__(self):
        return self.name
