from rest_framework import serializers
from payments.models import Tariff


class TariffShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tariff
        fields = ('id', 'title')