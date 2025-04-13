from django.urls import path
from profiles.apis import ProfileAPIView, CreateProfileAPIView, UpdateProfileAPIView, ReferalProgramAccountAPIView, ListProfilesPkAPIView

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
    )
]