from rest_framework.serializers import ModelSerializer

from spotterapi.models.Profile import Profile
from spotterapi.serializers.user_serializer import UserSerializer


class ProfileSerializer(ModelSerializer):
    
    user = UserSerializer()
        
    class Meta:
        model = Profile
        fields = ("user", "id", "bio", "created_on", "profile_image_url", "active", "profile_plans")
        

