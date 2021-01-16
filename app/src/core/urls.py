from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from django.views.generic import TemplateView, RedirectView
from accounts.views import LoginView, RegisterView, GuestRegisterView


urlpatterns = [

    path('accounts/', RedirectView.as_view(url='/account')),
    path('account/', include('accounts.urls', namespace='account')),
    path('accounts/', include('accounts.passwords.urls',)),
    path('login/', LoginView.as_view(), name='login'),
    path('register/guest', GuestRegisterView.as_view(), name='guest_register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
