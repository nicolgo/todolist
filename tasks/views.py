from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth.models import User

from tasks.serializers import TaskSerializer,UserSerializer
from tasks.permissions import IsOwnerOrReadOnly
from tasks.models import Task

class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated,IsOwnerOrReadOnly]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer