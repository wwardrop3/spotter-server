from django.db import models

class SessionExercise(models.Model):
    session = models.ForeignKey("Session", on_delete=models.CASCADE)
    exercise = models.ForeignKey("Exercise", on_delete = models.CASCADE)
    reps = models.IntegerField()
    sets = models.IntegerField()
    weight = models.IntegerField()
    distance = models.IntegerField()