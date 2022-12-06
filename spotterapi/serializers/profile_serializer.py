from rest_framework.serializers import ModelSerializer

from spotterapi.models.Profile import Profile


class ProfileSerializer(ModelSerializer):
        
    class Meta:
        model = Profile
        fields = ("id", "bio", "created_on", "profile_image_url", "active", "profile_plans")
        

