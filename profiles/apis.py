from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from profiles.models import Profile
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from profiles.serializers import ProfileSerializer, CreateProfileSerializer
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
        return Response(status=400)