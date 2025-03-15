from rest_framework.generics import ListAPIView, RetrieveAPIView
from payments.models import Tariff
from payments.serializers import TariffShortSerializer, TariffSerializer

class TariffsAPIView(ListAPIView):
    queryset = Tariff.objects.filter(is_published=True)
    serializer_class = TariffShortSerializer

class TariffAPIView(RetrieveAPIView):
    queryset = Tariff.objects.filter(is_published=True)
    lookup_field = 'pk'
    serializer_class = TariffSerializer