from rest_framework.viewsets import ViewSet
from spotterapi.models.Profile import Profile
from spotterapi.models.Session import Session
from spotterapi.models.SessionExercise import SessionExercise
from spotterapi.serializers.session_exercise_serializer import SessionExerciseSerializer
from spotterapi.models.Exercise import Exercise
from spotterapi.serializers.session_serializer import SessionSerializer
from rest_framework.response import Response
from rest_framework import status

class SessionView (ViewSet):
    
    def retrieve(self, request, pk):
        
        
        session = Session.objects.get(pk = pk)
        
        
        serializer = SessionSerializer(session)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    # dont need a list because all of the sessions will be attached to plans