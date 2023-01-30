from django.db import models
from django.utils.timezone import now
from datetime import date

# Create your models here.
class events(models.Model):
    event_title =  models.CharField(max_length=128, blank=False)
    event_date =  models.DateField(max_length=128, default=date.today,  editable=True)
    event_time = models.TimeField(auto_now=False, auto_now_add=False, default=now, editable=True)
    event_description =  models.CharField(max_length=628, blank=False)
    event_image = models.ImageField(upload_to='announcements/event_images', default="../media/announcements/event_images/default.jpg", blank=True)

    def __str__(self):
        return self.event_title

class work_blog(models.Model):
    work_title =  models.CharField(max_length=128, blank=False)
    work_summary =  models.CharField(max_length=128, blank=False)
    work_description =  models.CharField(max_length=628, blank=False)
    work_image = models.ImageField(upload_to='work_blog/work_images', default="../media/work_blog/work_images/default.jpg", blank=True)

    def __str__(self):
        return self.work_title