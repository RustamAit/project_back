from django.contrib.auth import authenticate
from django.shortcuts import render
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes, api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from api.models import *
from api.serializers import *
import json


@authentication_classes((TokenAuthentication,))
class BecomeAssigneeRequestView(viewsets.ModelViewSet):
    queryset = BecomeAssigneeRequest.objects.all()
    serializer_class = BecomeAssigneeRequestSerializer


@authentication_classes((TokenAuthentication,))
class ExpertList(viewsets.ModelViewSet):
    queryset = Expert.objects.all()
    serializer_class = ExpertSerializer


@authentication_classes((TokenAuthentication,))
class AssigneeList(viewsets.ModelViewSet):
    queryset = Assignee.objects.all()
    serializer_class = AssigneeSerializer


@authentication_classes((TokenAuthentication,))
class TaskList(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


@authentication_classes((TokenAuthentication,))
class UserList(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=status.HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=status.HTTP_404_NOT_FOUND)
    else:
        user_groups = []
        for i in user.groups.all():
            user_groups.append(i)
        print(user_groups[0])
        token, _ = Token.objects.get_or_create(user=user)
        res_body = {}
        res_body['token'] = token.key
        res_body['user_type'] = str(user_groups[0])
        res_body['user_id'] = user.id
        return Response(res_body,
                    status=status.HTTP_200_OK)


@api_view(['POST'])
def logout(request):
    request.auth.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@authentication_classes((TokenAuthentication,))
@api_view(['PUT'])
def addExecutor(request):
    taskId = request.GET["taskId"]
    userId = request.GET["userId"]
    task = Task.objects.get(pk=taskId)
    assignee = Assignee.objects.get(pk=userId)
    assignee.tasks.add(task)
    return Response({"success": True}, status=status.HTTP_200_OK)

