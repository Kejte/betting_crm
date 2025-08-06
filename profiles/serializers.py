from rest_framework import serializers
from profiles.models import Profile, ReferalProgramAccount, BookmakerFilterModel


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

class CreateBookmakerFilterSerializer(serializers.ModelSerializer):
     
    class Meta:
        model = BookmakerFilterModel
        fields = '__all__'

class ShortBookmakerFilterSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookmakerFilterModel
        fields = ('id', 'name')

class RetrieveBookmakerFilterSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        required=False
    )
    slug = serializers.CharField(
        required=False
    )

    class Meta:
        model = BookmakerFilterModel
        fields = ('id','max_coef_first_book', 'min_coef_first_book', 'max_coef_second_book', 'min_coef_second_book', 'name', 'slug', 'surebet_url', 'excluded_bookers')

