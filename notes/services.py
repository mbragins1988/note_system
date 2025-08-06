from .models import NotificationLog
from .notification_channels import send_email, send_sms, send_telegram


class NotificationService:
    @staticmethod
    def send_notification(notification):
        user_contact = notification.user.usercontactinfo

        # Порядок попыток отправки
        channels = [
            ('email', user_contact.email, send_email),
            ('sms', user_contact.phone, send_sms),
            ('telegram', user_contact.telegram_chat_id, send_telegram)
        ]

        for channel_name, contact_value, sender_func in channels:
            if not contact_value:
                continue

            try:
                sender_func(notification, contact_value)
                NotificationLog.objects.create(
                    notification=notification,
                    channel=channel_name,
                    status='success'
                )
                notification.is_sent = True
                notification.save()
                return True

            except Exception as e:
                NotificationLog.objects.create(
                    notification=notification,
                    channel=channel_name,
                    status='failed',
                    error_message=str(e)
                )
                continue

        notification.is_sent = False
        notification.save()
        return False
