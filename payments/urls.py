from django.urls import path
from payments.apis import TariffsAPIView, TariffAPIView, HasForkPermissionAPIView, CreatePaymentAPIView, UpdatePaymentAPIView, SubcriptionAPIView, ActivatedTrialPeriodAPIView, PromocodesAPIView, ActivatedPromocodeAPIView, PromocodeAPIView, CreateActivatedPromocodeAPIView, RetrieveActivatedPromocodeAPIView

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
    ),
    path(
        'activate_trial',
        ActivatedTrialPeriodAPIView.as_view()
    ),
    path(
        'promocodes',
        PromocodesAPIView.as_view()
    ),
    path(
        'activated_promocodes',
        ActivatedPromocodeAPIView.as_view()
    ),
    path(
        'promocode/<int:pk>',
        PromocodeAPIView.as_view()
    ),
    path(
        'activate_promocode',
        CreateActivatedPromocodeAPIView.as_view()
    ),
    path(
        'retrieve_activated_promocode',
        RetrieveActivatedPromocodeAPIView.as_view()
    )
]

