from django.urls import path
from notes.views import CreateNotificationView
from django.contrib import admin

urlpatterns = [
    path('api/notifications/', CreateNotificationView.as_view(), name='create-notification'),
    path('admin/', admin.site.urls),
]
