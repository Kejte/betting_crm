from rest_framework.generics import ListAPIView, RetrieveAPIView
from payments.models import Tariff, Payments, Subscription
from payments.serializers import TariffShortSerializer, TariffSerializer, CreatePaymentsSerializer, PaymentsSerializer
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from rest_framework.response import Response
from rest_framework.request import Request
import datetime

class TariffsAPIView(ListAPIView):
    queryset = Tariff.objects.filter(is_published=True)
    serializer_class = TariffShortSerializer

class TariffAPIView(RetrieveAPIView):
    queryset = Tariff.objects.filter(is_published=True)
    lookup_field = 'pk'
    serializer_class = TariffSerializer

class HasForkPermissionAPIView(APIView):

    @extend_schema(
    request=None,
    responses={
        200: None,
        400: None
    },
    parameters=[OpenApiParameter(
        name='tg_id',
        type=OpenApiTypes.STR,
        required=True
    )]
)
    def get(self, request, *args, **kwargs):
        if Payments.objects.filter(is_actual=True,subscription__profile__pk=self.request.query_params.get('tg_id')).exists():
            return Response(status=200)
        return Response(status=400)

class CreatePaymentAPIView(APIView):
    
    @extend_schema(
    request=CreatePaymentsSerializer,
    responses={
        200: None,
        400: None
    }
)
    def post(self, request: Request, *args, **kwargs):
        serializer = CreatePaymentsSerializer(data=request.data)
        if serializer.is_valid():
            sub, _ = Subscription.objects.get_or_create(profile=serializer.data['profile'])
            tariff = Tariff.objects.get(pk=serializer.data['tariff'])
            if not (Payments.objects.filter(subscription=sub,tariff=tariff,status=Payments.PaymentStatusChoice.IN_WORK).exists()) and not (Payments.objects.filter(subscription=sub,is_actual=True).exists()):
                payment = Payments.objects.create(
                    subscription=sub,
                    tariff= tariff,
                    expired_at=datetime.datetime.today() + datetime.timedelta(days=31.0)
                )
                return Response({'id': payment.pk},status=200)
            return Response(status=201)
        return Response(status=400)