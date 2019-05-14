from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from api.models import *
from api.serializers import *
import json


class BecomeAssigneeRequestView(viewsets.ModelViewSet):
    queryset = BecomeAssigneeRequest.objects.all()
    serializer_class = BecomeAssigneeRequestSerializer


class ExpertList(viewsets.ModelViewSet):
    queryset = Expert.objects.all()
    serializer_class = ExpertSerializer


class AssigneeList(viewsets.ModelViewSet):
    queryset = Assignee.objects.all()
    serializer_class = AssigneeSerializer


class TaskList(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class UserList(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
