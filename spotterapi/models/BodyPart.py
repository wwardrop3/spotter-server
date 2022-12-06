from django.db import models

class BodyPart(models.Model):
    name = models.TextField()
    body_section = models.ForeignKey("BodySection", on_delete = models.CASCADE) 