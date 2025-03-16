from django.urls import path
from feedback.apis import CreateTechSupportTicket, CreateUpdateTicketAPIView, UpdateLogAPIView

urlpatterns = [
    path(
        'create_tech_support_ticket',
        CreateTechSupportTicket.as_view()
    ),
    path(
        'create_update_ticket',
        CreateUpdateTicketAPIView.as_view()
    ),
    path(
        'update_log',
        UpdateLogAPIView.as_view()
    )
]