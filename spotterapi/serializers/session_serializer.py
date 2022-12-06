from rest_framework.serializers import ModelSerializer
from spotterapi.serializers.session_exercise_serializer import SessionExerciseSerializer
from spotterapi.models.Session import Session
from spotterapi.serializers.exercise_serializer import ExerciseSerializer

class SessionSerializer(ModelSerializer):
    
    

    class Meta:
        model = Session
        fields = ("id", "start_date", "exercises", "session_exercises")
        depth = 1

        