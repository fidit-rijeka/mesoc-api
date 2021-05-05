from django.urls import include, path

from rest_framework.routers import SimpleRouter

from .views.aggregate import AggregateHeatmapView, AggregateLocationView, AggregateCellSimilarityView
from .views.cell import CellViewSet
from .views.location import LocationViewSet
from .views.document import DocumentViewSet
from .views.feedback import FeedbackView
from .views.language import LanguageViewSet
from .views.login import LoginView
from .views.user import UserViewSet
from .views.password import PasswordResetViewSet
from .views.verification import VerificationViewSet


router = SimpleRouter()
router.register('account/verification', VerificationViewSet, basename='verification')
router.register('account/password_reset', PasswordResetViewSet, basename='password-reset')
router.register('cells', CellViewSet)
router.register('locations', LocationViewSet)
router.register('languages', LanguageViewSet)
router.register('documents', DocumentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('account/login/', LoginView.as_view()),
    path(
        'account/',
        UserViewSet.as_view({'get': 'retrieve', 'post': 'create', 'patch': 'partial_update'}),
        name='account',
    ),
    path('aggregates/location/', AggregateLocationView().as_view(), name='aggregate-location'),
    path('aggregates/heatmap/', AggregateHeatmapView().as_view(), name='aggregate-heatmap'),
    path('aggregates/similar/cell/', AggregateCellSimilarityView().as_view(), name='aggregate-similar'),
    path('feedback/', FeedbackView.as_view())
]
