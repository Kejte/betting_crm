from django.urls import path
from payments.apis import TariffsAPIView, TariffAPIView, HasForkPermissionAPIView, CreatePaymentAPIView, UpdatePaymentAPIView, SubcriptionAPIView

urlpatterns = [ 
    path(
        'tariffs',
        TariffsAPIView.as_view()
    ),
    path(
        'tariff/<int:pk>',
        TariffAPIView.as_view()
    ),
    path(
        'fork_permission',
        HasForkPermissionAPIView.as_view()
    ),
    path(
        'create_purchase_request',
        CreatePaymentAPIView.as_view()
    ),
    path(
        'update_payment',
        UpdatePaymentAPIView.as_view()
    ),
    path(
        'subscription',
        SubcriptionAPIView.as_view()
    )
]