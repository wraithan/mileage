from django.db import models


class Trip(models.Model):
    when = models.DateField()
    start = models.CharField(max_length=255)
    end = models.CharField(max_length=255)
    miles = models.DecimalField(max_digits=4, decimal_places=1)
    
    def __unicode__(self):
        return "%s, %s->%s, %s miles" % (self.when, self.start, self.end, self.miles)
