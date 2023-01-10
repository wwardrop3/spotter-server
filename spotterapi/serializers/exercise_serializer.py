

from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from spotterapi.models.Exercise import Exercise

class ExerciseSerializer(ModelSerializer):
    
    class Meta:
        model = Exercise
        fields = ("id", "name", "body_part", "machine", "type")
        
        
        
