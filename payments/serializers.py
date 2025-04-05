from rest_framework import serializers
from payments.models import Tariff, Payments, ActivatedTrialPeriod, Promocode, ActivatedPromocode
from profiles.models import Profile
from backend.settings import DOMEN

class TariffShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tariff
        fields = ('id', 'title')

class TariffSerializer(serializers.ModelSerializer):
    photo =  serializers.SerializerMethodField('_photo')

    class Meta:
        model = Tariff
        fields = '__all__'
    
    def _photo(self, instance: Tariff):
        return f'http://{DOMEN}/{instance.photo.url}'

class CreatePaymentsSerializer(serializers.Serializer):
    profile = serializers.PrimaryKeyRelatedField(
        queryset=Profile.objects.all()
    )
    tariff = serializers.PrimaryKeyRelatedField(
        queryset=Tariff.objects.filter(is_published=True)
    )
    promocode = serializers.PrimaryKeyRelatedField(
        queryset=Promocode.objects.filter(is_active=True),
        required=False
    )

class PaymentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payments
        fields = '__all__'

class ActivatedTrialPeriodSerializer(serializers.ModelSerializer):

    class Meta:
        model = ActivatedTrialPeriod
        fields = '__all__'

class PromocodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Promocode
        exclude = ('is_active',)

class PromocodeShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = Promocode
        fields = ('promo','id')

class ActivatedPromocodeSerialzier(serializers.ModelSerializer):

    class Meta:
        model = ActivatedPromocode
        exclude = ('buyed',)