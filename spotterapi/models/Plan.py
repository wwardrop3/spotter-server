from django.db import models



class Plan(models.Model):
    profile = models.ForeignKey("Profile", on_delete = models.CASCADE)
    exercises = models.ManyToManyField("Exercise", through = "PlanExercise")
    start_date = models.DateTimeField()
    public = models.BooleanField(False)
    stand_alone = models.BooleanField(False)
    
    

    @property
    def plan_sessions(self):
        return self.__plan_sessions
    @plan_sessions.setter
    def plan_sessions(self, value):
        self.__plan_sessions = value