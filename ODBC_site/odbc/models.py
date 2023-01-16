from django.db import models

# Create your models here.
class events(models.Model):
    event_title =  models.CharField(max_length=128)
    event_date =  models.DateTimeField(max_length=128)
    event_description =  models.CharField(max_length=628)
    event_image = models.ImageField(upload_to='announcements/event_images', default="../media/announcements/event_images/default.jpg", blank=True)

    def __str__(self):
        return self.event_title