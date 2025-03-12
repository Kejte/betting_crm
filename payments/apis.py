from rest_framework.generics import ListAPIView
from payments.models import Tariff
from payments.serializers import TariffShortSerializer

class TariffsAPIView(ListAPIView):
    queryset = Tariff.objects.filter(is_published=True)
    serializer_class = TariffShortSerializer