from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Meeting(models.Model):
    meetingtitle=models.CharField(max_length=255)
    meetingdate=models.DateField()
    meetingtime=models.TimeField()
    meetinglocation=models.CharField(max_length=255)
    meetingagenda=models.CharField(max_length=255)

    def __str__(self):
        return self.meetingtitle
    
    class Meta:
        db_table='Meeting'
    
class MeetingMinutes(models.Model):
    meetingid=models.ForeignKey(Meeting, on_delete=models.CASCADE)
    attendance=models.ManyToManyField(User)
    minutes=models.TextField()

    def __str__(self):
        return self.meetingid
    
    class Meta:
        db_table='MeetingMinutes'

class Resource(models.Model):
    resourcename=models.CharField(max_length=255)
    resourcetype=models.CharField(max_length=255)
    url=models.URLField(null=True, blank=True)
    dateentered=models.DateField()
    userid=models.ForeignKey(User, on_delete=models.CASCADE)
    description=models.CharField(max_length=255)

    def __str__(self):
        return self.resourcename

    class Meta:
        db_table='Resource'

class Event(models.Model):
    eventtitle:models.CharField(max_length=255)
    location:models.CharField(max_length=255)
    date:models.DateField()
    time:models.TimeField()
    description:models.CharField(max_length=255)
    userid:models.CharField(max_length=255)

    def __str__(self):
        return self.eventtitle

    class Meta:
        db_table='Event'

