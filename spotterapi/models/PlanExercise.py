from django.db import models

# the plan exercises will be the default so when a user starts a new session, the exercise stats will be default

class PlanExercise(models.Model):
    plan = models.ForeignKey("Plan", on_delete = models.CASCADE)
    exercise = models.ForeignKey("Exercise", on_delete = models.CASCADE)
    reps = models.IntegerField()
    sets = models.IntegerField()
    weight = models.IntegerField()
    distance = models.IntegerField()