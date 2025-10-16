"""octofit_tracker URL Configuration"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from rest_framework.documentation import include_docs_urls
from . import views

# Create router with custom root URL scheme
router = DefaultRouter()
router.register(r'api/users', views.UserViewSet, basename='user')
router.register(r'api/teams', views.TeamViewSet, basename='team')
router.register(r'api/activities', views.ActivityViewSet, basename='activity')
router.register(r'api/leaderboard', views.LeaderboardViewSet, basename='leaderboard')
router.register(r'api/workouts', views.WorkoutViewSet, basename='workout')

# Define base URL for API endpoints
API_URL = settings.CODESPACE_URL if settings.CODESPACE_URL else 'http://localhost:8000'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', views.api_root, name='api-root'),
    path('', include(router.urls)),
    path('docs/', include_docs_urls(title='OctoFit Tracker API', public=True)),
]
