from rest_framework import serializers

from tasks.models import Task
from django.contrib.auth.models import User

class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Task
        fields = ['id','owner','name','description','due_date','completed']

class UserSerializer(serializers.ModelSerializer):
    tasks = serializers.PrimaryKeyRelatedField(many=True,queryset=Task.objects.all())

    class Meta:
        model = User
        fields = ['id','username','tasks']