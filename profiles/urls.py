from django.urls import path
from profiles.apis import ProfileAPIView, CreateProfileAPIView, UpdateProfileAPIView, ReferalProgramAccountAPIView, ListProfilesPkAPIView, BookmakerFilterAPIView, RetrieveBookmakerFilterAPIView, FreebetFilterAPIView

urlpatterns = [ 
    path(
        'profile',
        ProfileAPIView.as_view()
    ),
    path(
        'profile/create',
        CreateProfileAPIView.as_view()
    ),
    path(
        'profile/update',
        UpdateProfileAPIView.as_view()
    ),
    path(
        'referal_account',
        ReferalProgramAccountAPIView.as_view()
    ),
    path(
        'profiles_pks',
        ListProfilesPkAPIView.as_view()
    ),
    path(
        'bookmaker_filter',
        BookmakerFilterAPIView.as_view()
    ),
    path(
        'bookmaker_filter/<int:pk>',
        RetrieveBookmakerFilterAPIView.as_view()
    ),
    path(
        'freebet_filter',
        FreebetFilterAPIView.as_view()
    )
]