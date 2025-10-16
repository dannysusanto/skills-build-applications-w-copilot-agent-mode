"""octofit_tracker URL Configuration"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from . import views

# Create router with custom root URL scheme
router = DefaultRouter()
router.register(r'api/users', views.UserViewSet, basename='user')
router.register(r'api/teams', views.TeamViewSet, basename='team')
router.register(r'api/activities', views.ActivityViewSet, basename='activity')
router.register(r'api/leaderboard', views.LeaderboardViewSet, basename='leaderboard')
router.register(r'api/workouts', views.WorkoutViewSet, basename='workout')

# Override router URLs to use HTTPS when in Codespace
if settings.CODESPACE_URL:
    router.root_view_name = 'api-root'
    router.urls[0].pattern._route = 'api/'
    router.urls[0].pattern._regex = '^api/$'
    router.urls[0].name = 'api-root'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', views.api_root),
    path('', include(router.urls)),
]
