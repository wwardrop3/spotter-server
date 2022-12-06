from rest_framework.viewsets import ViewSet
from spotterapi.models.Profile import Profile
from spotterapi.models.Plan import Plan
from spotterapi.serializers.plan_serializer import PlanSerializer
from spotterapi.serializers.session_serializer import SessionSerializer
from spotterapi.serializers.session_exercise_serializer import SessionExerciseSerializer
from rest_framework import status
from rest_framework.response import Response
from spotterapi.models.Session import Session
from spotterapi.models.SessionExercise import SessionExercise


class PlanView (ViewSet):
    
    def list(self, request):
        
        profile = Profile.objects.get(user = request.auth.user)
        
        plans = Plan.objects.filter(profile = profile)
        
        for i in range(0, len(plans)):
            plans[i].plan_sessions = SessionSerializer(Session.objects.filter(plan = plans[i].id), many = True).data
        
      
        
        
        
        
        
        serializer = PlanSerializer(plans, many = True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def retrieve (self, request, pk):
        
        # Get the plan object from the pk sent in the url
        plan = Plan.objects.get(pk = pk)
        
        # Get all sessions related to plan
        sessions = Session.objects.filter(plan = plan)
        
        # need to add all of the session_exercises on
        for i in range(0, len(sessions)):
            session_exercises = SessionExercise.objects.filter(session = sessions[i].id)
            session_exercise_serializer = SessionExerciseSerializer(session_exercises, many = True)
            sessions[i].session_exercises = session_exercise_serializer.data
            print(sessions[i].exercises)
        
        
        # Serialize the sessions before attaching to the plan object
        session_serializer = SessionSerializer(sessions, many = True)
        
        # Attach sessions to the plan
        plan.plan_sessions = session_serializer.data
   
        # Serialize final plan
        serializer = PlanSerializer(plan)
        

        
        return Response(serializer.data, status=status.HTTP_200_OK)