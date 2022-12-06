
from rest_framework.serializers import ModelSerializer
from spotterapi.models.SessionExercise import SessionExercise

class SessionExerciseSerializer(ModelSerializer):
    

    class Meta:
        model = SessionExercise
        fields = ("id", "reps", "weight", "exercise", "session", "sets")
        depth = 1