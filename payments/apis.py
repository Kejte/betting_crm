from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from payments.models import Tariff, Payments, Subscription, ActivatedTrialPeriod, Promocode, ActivatedPromocode, ObservedTopic, ObservedTopicSettings
from payments.serializers import TariffShortSerializer, TariffSerializer, CreatePaymentsSerializer, ActivatedTrialPeriodSerializer, PromocodeSerializer, PromocodeShortSerializer, ActivatedPromocodeSerialzier, ObservedTopicSerializer, ObservedTopicSettingSerializer, UpdateObservedTopicSettingsSerializer
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from rest_framework.response import Response
from rest_framework.request import Request
import datetime
from profiles.models import Profile, ReferalProgramAccount


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
            sub, _ = Subscription.objects.get_or_create(profile=Profile.objects.get(pk=serializer.data['profile']))
            tariff = Tariff.objects.get(pk=serializer.data['tariff'])
            try:
                promo = Promocode.objects.get(pk=serializer.data['promocode'])
            except Exception:
                promo = None
            if not (Payments.objects.filter(subscription=sub,tariff=tariff,status=Payments.PaymentStatusChoice.IN_WORK).exists()) and not (Payments.objects.filter(subscription=sub,is_actual=True).exists()):
                payment = Payments.objects.create(
                    subscription=sub,
                    tariff= tariff,
                    expired_at=datetime.datetime.today() + datetime.timedelta(days=float(tariff.duration+1)),
                    promocode=promo
                )
                return Response({'id': payment.pk},status=200)
            return Response(status=201)
        return Response(status=400)

class UpdatePaymentAPIView(APIView):

    @extend_schema(
            request=None,
            responses={
                200: None
            },
            parameters=[
                OpenApiParameter(name='payment_id', type=OpenApiTypes.INT, required=True),
                OpenApiParameter(name='action', type=OpenApiTypes.STR, required=True)
            ]
    )
    def put(self, request: Request, *args, **kwargs):
        action = self.request.query_params.get('action')
        payment = Payments.objects.get(pk=self.request.query_params.get('payment_id'))
        match action:
            case 'accept':
                payment.status = Payments.PaymentStatusChoice.ACCEPTED
                payment.is_actual = True
                if payment.promocode:
                    payment.promocode.remained -= 1
                    payment.promocode.save()
                if payment.subscription.profile.referrer:
                    ref = ReferalProgramAccount.objects.get(profile__pk=payment.subscription.profile.referrer.pk)
                    cost = payment.tariff.cost if not payment.promocode else payment.tariff.cost - payment.promocode.discount
                    ref.balance += cost * 0.4
                    ref.total_earnings += cost * 0.4
                    ref.save()
                payment.save()
            case 'cancel':
                payment.status = Payments.PaymentStatusChoice.CANCELED
                payment.save()
        return Response(status=200)

class SubcriptionAPIView(APIView):

    @extend_schema(
            request=None,
            responses={
                200: {
                    'tariff': str,
                    'remained_days': int,
                    'cost': int
                }
            },
            parameters=[
                OpenApiParameter(name='tg_id',type=OpenApiTypes.INT, required=True)
            ]
    )
    def get(self, request: Request, *args, **kwargs):
        try:
            payment = Payments.objects.get(subscription__profile__pk=self.request.query_params.get('tg_id'),is_actual=True)
            return Response(
                {
                'tariff': payment.tariff.title,
                'remained_days': (payment.expired_at - datetime.datetime.today().date()).days,
                'cost': payment.tariff.cost,
                'is_private': payment.tariff.is_private
                }
            )
        except Payments.DoesNotExist:
            return Response(status=400)

class ActivatedTrialPeriodAPIView(APIView):
    
    @extend_schema(
            request=None,
            responses={
                200: None,
                201: None
            },
            parameters=[
                OpenApiParameter(name='tg_id', type=OpenApiTypes.INT, required=True),
                OpenApiParameter(name='tariff_id', type=OpenApiTypes.INT, required=True)
            ]
    )
    def get(self, request, *args, **kwargs):
        return Response(status=200) if ActivatedTrialPeriod.objects.filter(profile=self.request.query_params.get('tg_id'), tariff=self.request.query_params.get('tariff_id')).exists() else Response(status=201)

    def post(self, request, *args, **kwargs):
        serializer = ActivatedTrialPeriodSerializer(data=request.data)
        if serializer.is_valid():
            sub, _ = Subscription.objects.get_or_create(profile=serializer.validated_data['profile'],)
            Payments.objects.create(
                subscription=sub,
                tariff=serializer.validated_data['tariff'],
                expired_at=datetime.datetime.today() + datetime.timedelta(days=4),
                is_actual=True,
                status=Payments.PaymentStatusChoice.ACCEPTED
            )
            serializer.save()
            return Response(status=200)
        return Response(serializer.errors,status=400)

class PromocodesAPIView(APIView):
    
    @extend_schema(
        request=None,
        responses={
            200: None
        },
        parameters=[
            OpenApiParameter(name='tariff_id', type=OpenApiTypes.INT, required=True),
        ]
    )
    def get(self, request: Request, *args, **kwargs):
        tariff_id = request.query_params.get('tariff_id')
        promocodes = Promocode.objects.filter(tariff__pk=tariff_id, is_active=True)
        serializer = PromocodeShortSerializer(promocodes, many=True)
        return Response(serializer.data,200)

class PromocodeAPIView(RetrieveAPIView):
    serializer_class = PromocodeSerializer
    queryset = Promocode.objects.filter()
    lookup_field = 'pk'

class ActivatedPromocodeAPIView(APIView):

    @extend_schema(
            request=None,
            responses={
                200: None,
                201: None
            },
            parameters=[
                OpenApiParameter(name='tariff_id', type=OpenApiTypes.INT, required=True),
                OpenApiParameter(name='tg_id', type=OpenApiTypes.INT, required=True)
            ]
    )
    def get(self, request: Request, *args, **kwargs):
        tariff_id = request.query_params.get('tariff_id')
        tg_id = request.query_params.get('tg_id')
        if ActivatedPromocode.objects.filter(promocode__tariff__pk=tariff_id, profile__pk=tg_id, buyed=False).exists():
            return Response(status=201)
        return Response(status=200)

class CreateActivatedPromocodeAPIView(CreateAPIView):
    serializer_class = ActivatedPromocodeSerialzier
    queryset = ActivatedPromocode.objects.all()

class RetrieveActivatedPromocodeAPIView(APIView):
    
    @extend_schema(
        request=None,
        responses={
            200: PromocodeSerializer,
            201: None
        },
        parameters=[
            OpenApiParameter(name='tariff_id', type=OpenApiTypes.INT, required=True),
            OpenApiParameter(name='tg_id', type=OpenApiTypes.INT, required=True)
        ]
    )
    def get(self, request: Request, *args, **kwargs):
        try:
            activated_promo = ActivatedPromocode.objects.get(
                profile__pk=request.query_params.get('tg_id'),
                promocode__tariff__pk=request.query_params.get('tariff_id'), 
                buyed=False
            )
            if activated_promo.promocode.is_active:
                return Response(PromocodeSerializer(Promocode.objects.get(pk=activated_promo.promocode.pk)).data, status=200)
            return Response(status=201)
        except ActivatedPromocode.DoesNotExist:
            return Response(status=201)

class ListObservedTopics(ListAPIView):
    queryset = ObservedTopic.objects.all()
    serializer_class = ObservedTopicSerializer

class ObservedTopicSettingAPIView(APIView):

    @extend_schema(
        request=None,
        responses={
            200: ObservedTopicSettingSerializer
        },
        parameters=[
            OpenApiParameter(name='tg_id', type=OpenApiTypes.INT, required=True),
            OpenApiParameter(name='topic_id', type=OpenApiTypes.INT, required=True)
        ]
    )
    def get(self, request: Request, *args, **kwargs):
        profile = Profile.objects.get(tg_id=request.query_params.get('tg_id'))
        topic = ObservedTopic.objects.get(pk=request.query_params.get('topic_id'))
        obj, _ = ObservedTopicSettings.objects.get_or_create(profile=profile,topic=topic)
        return Response(ObservedTopicSettingSerializer(obj).data,status=200)
    
    @extend_schema(
        request=UpdateObservedTopicSettingsSerializer,
        responses={
            200: ObservedTopicSettingSerializer,
            400: None
        },
        parameters=[
            OpenApiParameter(name='topic_id', type=OpenApiTypes.INT, required=True)
        ]
    )
    def put(self, request: Request, *args, **kwargs):
        serializer = UpdateObservedTopicSettingsSerializer(data=request.data)
        if serializer.is_valid():
            setting = ObservedTopicSettings.objects.get(pk=request.query_params.get('topic_id'))
            if serializer.data['max_profit']:
                setting.max_profit = serializer.data['max_profit']
            else:
                setting.min_profit = serializer.data['min_profit']
            try:
                if serializer.data['is_active'] != None:
                    setting.is_active = serializer.data['is_active']
            except KeyError:
                pass
            setting.save()
            return Response(ObservedTopicSettingSerializer(setting).data,200)
        return Response(serializer.errors,400)
