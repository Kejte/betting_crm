from django.urls import path
from payments.apis import TariffsAPIView

urlpatterns = [ 
    path(
        'tariffs',
        TariffsAPIView.as_view()
    ),
]