from rest_framework.generics import RetrieveAPIView, UpdateAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView
from profiles.models import Profile, ReferalProgramAccount, BookmakerFilterModel
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from profiles.serializers import ProfileSerializer, CreateProfileSerializer, UpdateProfileSerializer, ReferalProgramAccountSerializer, CreateReferalProgramAccountSerializer, ShortBookmakerFilterSerializer, CreateBookmakerFilterSerializer, RetrieveBookmakerFilterSerializer
from rest_framework.request import Request
from rest_framework.response import Response

class ProfileAPIView(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    @extend_schema(
    request=None,
    responses={
        200: ProfileSerializer,
        400: None
    },
    parameters=[OpenApiParameter(
        name='tg_id',
        type=OpenApiTypes.STR,
        required=True
    )]
)
    def get(self, request: Request, *args, **kwargs):
        try:
            profile = Profile.objects.get(tg_id=str(request.query_params.get('tg_id')))
            return Response(ProfileSerializer(profile).data,200)
        except Profile.DoesNotExist:
            return Response(status=400)

class CreateProfileAPIView(APIView):
    
    @extend_schema(
        request=CreateProfileSerializer,
        responses={
            200: CreateProfileSerializer,
            400: None
        }
    )
    def post(self, request: Request, *args, **kwargs):
        serializer = CreateProfileSerializer(data=request.data)
        if serializer.is_valid():
            profile = Profile.objects.create(**serializer.validated_data)
            return Response(ProfileSerializer(profile).data,200)
        print(serializer.errors)
        return Response(serializer.errors,status=400)

class UpdateProfileAPIView(APIView):
    
    @extend_schema(
        request=CreateProfileSerializer,
        responses={
            200: CreateProfileSerializer,
            400: None
        },
        parameters=[
            OpenApiParameter(
        name='tg_id',
        type=OpenApiTypes.STR,
        required=True
    )
        ]
    )
    def put(self, request: Request, *args, **kwargs):
        serializer = UpdateProfileSerializer(data=request.data)
        if serializer.is_valid():
            profile = Profile.objects.get(pk=request.query_params.get('tg_id'))
            profile.username = serializer.validated_data.pop('username')
            profile.save()
            return Response(status=201)
        return Response(serializer.errors,status=400)

class ReferalProgramAccountAPIView(APIView):

    @extend_schema(
        request=None,
        responses={
            200: ReferalProgramAccountSerializer,
            400: None
        },
        parameters=[
            OpenApiParameter(name='tg_id',type=OpenApiTypes.INT,required=True)
        ]
    )
    def get(self, request: Request, *args, **kwargs):
        try:
            account = ReferalProgramAccount.objects.get(profile__pk=request.query_params.get('tg_id'))
            return Response(ReferalProgramAccountSerializer(account).data,200)
        except ReferalProgramAccount.DoesNotExist:
            return Response(status=400)
    
    @extend_schema(
        request=CreateReferalProgramAccountSerializer,
        responses={
            200: ReferalProgramAccountSerializer,
            400: None
        }
    )
    def post(self, request: Request, *args, **kwargs):
        serializer = CreateReferalProgramAccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(ReferalProgramAccountSerializer(ReferalProgramAccount.objects.get(profile__pk=serializer.validated_data['profile'].pk)).data,200)
        return Response(serializer.errors,400)
    
    @extend_schema(
        request=None,
        responses={
            200: None
        },
        parameters=[
            OpenApiParameter(name='tg_id', type=OpenApiTypes.INT, required=True)
        ]
    )
    def put(self, request: Request, *args, **kwargs):
        ref = ReferalProgramAccount.objects.get(profile__pk=request.query_params.get('tg_id'))
        ref.balance = 0
        ref.save()
        return Response(status=200)

class ListProfilesPkAPIView(APIView):

    def get(self, request: Request, *args, **kwargs):
        ids = [profile.pk for profile in Profile.objects.all()]
        return Response({'profiles': ids}, 200)

class BookmakerFilterAPIView(APIView):

    @extend_schema(
        request=None,
        responses = {
            200: ShortBookmakerFilterSerializer,
            400: None
        },
        parameters=[
            OpenApiParameter(name='tg_id', type=OpenApiTypes.INT, required=True),
            OpenApiParameter(name='bookmaker_slug', type=OpenApiTypes.STR, required=True)
        ]
    )
    def get(self, request: Request, *args, **kwargs):
        qs = BookmakerFilterModel.objects.filter(profile__pk=request.query_params.get('tg_id'),slug=request.query_params.get('bookmaker_slug'))
        return Response(ShortBookmakerFilterSerializer(qs,many=True).data,200)

    @extend_schema(
        request=CreateBookmakerFilterSerializer,
        responses = {
            200: ShortBookmakerFilterSerializer,
            400: None
        }
    )
    def post(self, request: Request, *args, **kwargs):
        serializer = CreateBookmakerFilterSerializer(data=request.data)
        if serializer.is_valid():
            filter = serializer.save()
            print(filter)
            return Response(RetrieveBookmakerFilterSerializer(filter).data,status=200)
        return Response(serializer.error_messages,400)
    
    @extend_schema(
            request=None,
            responses={
                200: None,
                400: None
            },
            parameters=[
                OpenApiParameter(name='filter_id', type=OpenApiTypes.INT, required=True)
            ]
    )
    def delete(self, request: Request, *args, **kwargs):
        try:
            id = int(request.query_params.get('filter_id'))
            BookmakerFilterModel.objects.get(pk=id).delete()
            return Response(status=200)
        except Exception as e:
            return Response(e.args,400)

class RetrieveBookmakerFilterAPIView(RetrieveUpdateAPIView):
    serializer_class = RetrieveBookmakerFilterSerializer
    lookup_field = 'pk'
    queryset = BookmakerFilterModel.objects.all()

