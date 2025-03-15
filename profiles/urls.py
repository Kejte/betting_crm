from django.urls import path
from profiles.apis import ProfileAPIView, CreateProfileAPIView, UpdateProfileAPIView

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
    )
]