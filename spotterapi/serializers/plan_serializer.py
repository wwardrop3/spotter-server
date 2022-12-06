from rest_framework.serializers import ModelSerializer
from spotterapi.serializers.profile_serializer import ProfileSerializer
from spotterapi.models.Plan import Plan
from spotterapi.models.Session import Session


class PlanSerializer(ModelSerializer):
    
    plan_sessions = Session()
    
    class Meta:
        model = Plan
        fields = ("id", "exercises", "profile", "start_date", "public", "plan_sessions", "stand_alone")
        depth = 1
        

