from django.db import models

from spotterapi.models.Exercise import Exercise

class Session(models.Model):
    exercises = models.ManyToManyField(Exercise, through = "SessionExercise")
    plan = models.ForeignKey("Plan", on_delete=models.CASCADE)
    start_date = models.DateTimeField()

    
    @property
    def session_exercises(self):
        return self.__session_exercises
    @session_exercises.setter
    def session_exercises(self, value):
        self.__session_exercises = value