from django.urls import path

from .views import (
    AccountHomeView,
    AccountEmailActivateView,
    UserDetailUpdateView,
)

app_name = 'account'

urlpatterns = [
    path('', AccountHomeView.as_view(), name='home'),
    path('details/', UserDetailUpdateView.as_view(), name='user-update'),
    path('email/confirm/<key>/', AccountEmailActivateView.as_view(), name='email-activate'),
    path('email/resend-activation/', AccountEmailActivateView.as_view(), name='resend-activation'),
]

# account/email/confirm/asdfads/ -> activation view
