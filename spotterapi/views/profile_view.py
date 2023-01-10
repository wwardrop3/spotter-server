from rest_framework.viewsets import ViewSet
from spotterapi.models.Profile import Profile
from spotterapi.models.Plan import Plan
from spotterapi.serializers.profile_serializer import ProfileSerializer
from spotterapi.serializers.plan_serializer import PlanSerializer

from rest_framework import status
from rest_framework.response import Response
from spotterapi.models.Session import Session


class ProfileView (ViewSet):
    
    def retrieve(self, request, pk):
        
        profile = Profile.objects.get(user = request.auth.user)
        
        plans = Plan.objects.filter(profile = profile.id)
        
        plan_serializer = PlanSerializer(plans, many = True)
        
        profile.profile_plans = plan_serializer.data
        
        serializer = ProfileSerializer(profile)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
        

    def list(self, request):
        
        profile = Profile.objects.get(user = request.auth.user)
        
                
        serializer = ProfileSerializer(profile)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    