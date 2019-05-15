from django.contrib.auth import authenticate, logout
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import authentication_classes, api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, generics
from api.models import *
from api.serializers import *
import json


@authentication_classes((TokenAuthentication,))
class BecomeAssigneeRequestView(viewsets.ModelViewSet):
    queryset = BecomeAssigneeRequest.objects.all()
    serializer_class = BecomeAssigneeRequestSerializer


class BecomeAssigneeRequestList(APIView):
    def get(self, request):
        categories = BecomeAssigneeRequest.objects.all()
        serializer = BecomeAssigneeRequestSerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BecomeAssigneeRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def put(self, request, pk, format=None):
        snippet = BecomeAssigneeRequest.objects.get_object(pk)
        serializer = BecomeAssigneeRequestSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = BecomeAssigneeRequest.objects.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TaskView(APIView):

    def get(self, request):
        categories = Task.objects.all()
        serializer = TaskSerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def put(self, request, pk, format=None):
        snippet = Task.objects.get_object(pk)
        serializer = TaskSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = Task.objects.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@authentication_classes((TokenAuthentication,))
class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskReadSerialize

    def create(self, request, *args, **kwargs):
        created_by = request.data.get("created_by")
        task_status = request.data.get("status")
        address = request.data.get("address")
        description = request.data.get('description')
        title = request.data.get('title')
        task = Task(title = title, description = description, address=address,
                    created_by=Expert.objects.get(pk=created_by), status = Status.objects.get(pk = 2) )
        task.save()
        return Response({"success: true"}, status=status.HTTP_200_OK)




class TaskArray(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskReadSerialize




@authentication_classes((TokenAuthentication,))
class ExpertList(viewsets.ModelViewSet):
    queryset = Expert.objects.all()
    serializer_class = ExpertSerializer


@authentication_classes((TokenAuthentication,))
class AssigneeList(viewsets.ModelViewSet):
    queryset = Assignee.objects.all()
    serializer_class = AssigneeSerializer

@authentication_classes((TokenAuthentication,))
class UserList(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(["POST"])
@permission_classes((AllowAny,))
def login_view(request):
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
        expert = Expert.objects.get(user = user)
        res_body['token'] = token.key
        res_body['user_type'] = str(user_groups[0])
        res_body['user_id'] = expert.id
        return Response(res_body, status=status.HTTP_200_OK)


@api_view(['POST'])
def logout_view(request):
    logout(request)
    return Response({"success": True}, status=status.HTTP_204_NO_CONTENT)

@authentication_classes((TokenAuthentication,))
@api_view(['PUT'])
def addExecutor(request):
    taskId = request.GET["taskId"]
    userId = request.GET["userId"]
    task = Task.objects.get(pk=taskId)
    assignee = Assignee.objects.get(pk=userId)
    assignee.tasks.add(task)
    return Response({"success": True}, status=status.HTTP_200_OK)

