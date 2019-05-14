from rest_framework import serializers

from api.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class BecomeAssigneeRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = BecomeAssigneeRequest
        fields = "__all__"


class ExpertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expert
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


class AssigneeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignee
        fields = "__all__"


class StatusSerializer(serializers.Serializer):
    status_name = serializers.CharField()
    status_color = serializers.CharField()
