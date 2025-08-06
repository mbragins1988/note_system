def send_email(notification, email):
    # В реальности здесь будет вызов реального email-сервиса
    print(f"Sending email to {email}: {notification.subject}")

    # Имитация случайной ошибки для тестирования, расклментируйте
    # raise Exception("Email service unavailable")


def send_sms(notification, phone):
    print(f"Sending SMS to {phone}: {notification.message}")

    # Имитация случайной ошибки для тестирования, расклментируйте
    # raise Exception("SMS service unavailable")


def send_telegram(notification, chat_id):
    print(f"Sending Telegram to {chat_id}: {notification.message}")

    # Имитация случайной ошибки для тестирования, расклментируйте
    # raise Exception("Telegram API error")
