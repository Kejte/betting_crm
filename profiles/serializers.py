from rest_framework import serializers
from profiles.models import Profile, ReferalProgramAccount


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('tg_id', 'username')

class CreateProfileSerializer(serializers.ModelSerializer):
    referrer = serializers.PrimaryKeyRelatedField(
        queryset = Profile.objects.all(),
        required=False
    )

    class Meta:
        model = Profile
        fields = ('tg_id', 'username', 'referrer')

class UpdateProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False)
    referrer = serializers.PrimaryKeyRelatedField(
        queryset = Profile.objects.all(),
        required=False
    )

    class Meta:
        model = Profile
        fields = ('username', 'referrer')

class ReferalProgramAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReferalProgramAccount
        exclude = ('id',)

class CreateReferalProgramAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReferalProgramAccount
        fields = ('profile', 'referal_url')