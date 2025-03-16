from rest_framework import serializers
from feedback.models import TechSupportTicket, UpdateTicket# UpdateLog
from profiles.models import Profile

class TechSupportTicketSerializer(serializers.ModelSerializer):
    profile = serializers.PrimaryKeyRelatedField(
        queryset=Profile.objects.all()
    )

    class Meta:
        model = TechSupportTicket
        fields = ('profile', 'text')

class UpdateTicketSerializer(serializers.ModelSerializer):
    profile = serializers.PrimaryKeyRelatedField(
        queryset=Profile.objects.all()
    )

    class Meta:
        model = UpdateTicket
        fields = ('profile', 'text')

# class UpdateLogSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = UpdateLog
#         exclude = ('id','is_published')