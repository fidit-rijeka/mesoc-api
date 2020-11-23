from django.urls import include, path

from rest_framework.routers import SimpleRouter

from .views.feedback import FeedbackView
from .views.login import LoginView
from .views.user import UserViewSet
from .views.password import PasswordResetViewSet
from .views.verification import VerificationViewSet


router = SimpleRouter()
router.register('users', UserViewSet)
router.register('account/verification', VerificationViewSet, basename='verification')
router.register('account/password_reset', PasswordResetViewSet, basename='password-reset')

urlpatterns = [
    path('', include(router.urls)),
    path('account/login/', LoginView.as_view()),
    path('feedback/', FeedbackView.as_view())
]
