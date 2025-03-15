from django.urls import path
from payments.apis import TariffsAPIView, TariffAPIView

urlpatterns = [ 
    path(
        'tariffs',
        TariffsAPIView.as_view()
    ),
    path(
        'tariff/<int:pk>',
        TariffAPIView.as_view()
    )
]