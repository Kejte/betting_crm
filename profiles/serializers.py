from rest_framework import serializers
from profiles.models import Profile


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('tg_id', 'username')

class CreateProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        fields = ('tg_id', 'username')

class UpdateProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        fields = ('username',)