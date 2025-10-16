"""octofit_tracker URL Configuration"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'api/users', views.UserViewSet)
router.register(r'api/teams', views.TeamViewSet)
router.register(r'api/activities', views.ActivityViewSet)
router.register(r'api/leaderboard', views.LeaderboardViewSet)
router.register(r'api/workouts', views.WorkoutViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', views.api_root),
    path('', include(router.urls)),
]
