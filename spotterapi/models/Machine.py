from django.db import models

class Machine(models.Model):
    name = models.TextField()
    image_url = models.TextField()
    video_url = models.TextField()
    