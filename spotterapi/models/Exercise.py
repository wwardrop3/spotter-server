
from django.db import models

class Exercise(models.Model):
    name = models.TextField()
    machine = models.ForeignKey("Machine", on_delete = models.CASCADE)
    body_part = models.ForeignKey("BodyPart", on_delete = models.CASCADE)
    type = models.ForeignKey("Type", on_delete = models.CASCADE)
    
    
    
    # # When an exercise is called, want to pull stats related to the exercise and the user or plan
    
    # @property
    # def avg_weight(self):
    #     return self.__avg_weight
    
    # @avg_weight.setter
    # def avg_weight(self, value):
    #     self.avg_weight = value
    
    
    
    # # this shows the count of all the exercises////temporary
    # @property
    # def count(self):
    #     return self.__count
    # def count (self, value):
    #     self.count = value
    
    
    