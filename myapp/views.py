# myapp/views.py
from rest_framework import viewsets
from .models import Updates, LatestNews, OurTeam, BoardTeam
from .serializers import UpdatesSerializer, LatestNewsSerializer, OurTeamSerializer, BoardTeamSerializer

# ViewSet for Updates
class UpdatesViewSet(viewsets.ModelViewSet):
    queryset = Updates.objects.all()
    serializer_class = UpdatesSerializer

# ViewSet for Latest News
class LatestNewsViewSet(viewsets.ModelViewSet):
    queryset = LatestNews.objects.all()
    serializer_class = LatestNewsSerializer

# ViewSet for Our Team
class OurTeamViewSet(viewsets.ModelViewSet):
    queryset = OurTeam.objects.all()
    serializer_class = OurTeamSerializer

# ViewSet for Board Team
class BoardTeamViewSet(viewsets.ModelViewSet):
    queryset = BoardTeam.objects.all()
    serializer_class = BoardTeamSerializer
