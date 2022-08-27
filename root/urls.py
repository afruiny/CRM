from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from leads.views import LandingPageView
from leads.views import SignUpView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView, PasswordResetView
from django.contrib.auth.views import PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetCompleteView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name='landing-page'),
    path('leads/', include('leads.urls', namespace='leads')),
    path('login/',LoginView.as_view(),name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(),name='logout'),
    path('password-reset/', PasswordResetView.as_view(),name='password-reset'),
    path('password-reset-done/', PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('password-reset-confirm/<uib64>/<token>/', PasswordResetConfirmView.as_view(), name='password_resert_confirm'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(),name='password_reset_confirm'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)








