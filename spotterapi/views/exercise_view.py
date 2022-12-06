from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from spotterapi.models.SessionExercise import SessionExercise

from spotterapi.models.Exercise import Exercise
from spotterapi.serializers.exercise_serializer import ExerciseSerializer
from rest_framework.response import Response
from rest_framework import status

class ExerciseView(ViewSet):
    
    def list(self, request):
        # This will be used when a user is selecting individual exercises to add to a workout plan
        # first get the object from the exercise model that has an id that matches pk
        
        exercises = Exercise.objects.all()
        
        count = len(exercises)
        
        for i in range(0, len(exercises)):
            exercises[i].count = count
        
        # want to get stats of each exercise as they relate to the user
            # average_weight
        
        # for i in exercises:
        #     # for each unique exercise from the database
        #     session_exercises = SessionExercise.objects.filter(pk = exercises[i].exercise)
            
        #     # get how many times the user did the exercise
        #     exercise_count = len(session_exercises)
        #     exercise_weights = 0
            
        #     for j in session_exercises:
        #         # for each instance of the user doing the exercise
        #         exercise_weights += session_exercises[j].weight
            
        #     all_session_exercises[i].avg_weight = exercise_weights / exercise_count
        
        
        
        serializer = ExerciseSerializer(exercises, many = True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
        
        
        
        
        
        
        
        
        
    
    
    
