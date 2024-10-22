# myapp/urls.py
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'updates', views.UpdatesViewSet, basename='updates')
router.register(r'news', views.LatestNewsViewSet, basename='news')
router.register(r'our-team', views.OurTeamViewSet, basename='our-team')
router.register(r'board-team', views.BoardTeamViewSet, basename='board-team')

# The API URLs are now determined automatically by the router
urlpatterns = router.urls
