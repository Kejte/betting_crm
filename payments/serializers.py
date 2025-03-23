from rest_framework import serializers
from payments.models import Tariff, Payments
from profiles.models import Profile


class TariffShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tariff
        fields = ('id', 'title')

class TariffSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tariff
        fields = '__all__'

class CreatePaymentsSerializer(serializers.Serializer):
    profile = serializers.PrimaryKeyRelatedField(
        queryset=Profile.objects.all()
    )
    tariff = serializers.PrimaryKeyRelatedField(
        queryset=Tariff.objects.filter(is_published=True)
    )

class PaymentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payments
        fields = '__all__'
        
