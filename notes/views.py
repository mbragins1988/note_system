from rest_framework import generics, status
from rest_framework.response import Response
from .models import Notification
from .serializers import NotificationSerializer
from .services import NotificationService


class CreateNotificationView(generics.CreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        notification = serializer.save()

        NotificationService.send_notification(notification)

        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )
