from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from feedback.serializers import TechSupportTicketSerializer, UpdateTicketSerializer, UpdateLogSerializer
from feedback.models import TechSupportTicket, UpdateTicket, UpdateLog
from rest_framework.response import Response

class CreateTechSupportTicket(CreateAPIView):
    serializer_class = TechSupportTicketSerializer
    queryset = TechSupportTicket.objects.all()

class CreateUpdateTicketAPIView(CreateAPIView):
    serializer_class = UpdateTicketSerializer
    queryset = UpdateTicket.objects.all()

class UpdateLogAPIView(APIView):
    serializer_class = UpdateLogSerializer

    def get(self, request, *args, **kwargs):
        try:
            queryset = UpdateLog.objects.filter(is_published=True).latest('created_at')
            serializer = self.serializer_class(queryset)
            return Response(serializer.data,200)
        except Exception:
            return Response(status=400)