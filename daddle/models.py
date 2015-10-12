from django.db import models

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    min_people = models.IntegerField()
    max_people = models.IntegerField()

    def __str__(self):
        return "%s (%s)" % (self.title, self.start_date)

