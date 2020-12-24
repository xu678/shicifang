from django.urls import path
from apps.users.views.register import RegisterApiView


urlpatterns = [
    path("users/", RegisterApiView.as_view()),
    path("sms_codes/<mobile>/", GetSmsApiView.as_view())
]