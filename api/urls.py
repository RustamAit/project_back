from django.urls import path, include
from rest_framework import routers

from api import views


router = routers.DefaultRouter()
router.register('users', views.UserList)
router.register('tasks', views.TaskList)
router.register('experts', views.ExpertList)
router.register('assignees', views.AssigneeList)
router.register('BecomeAssigneeRequests', views.BecomeAssigneeRequestView)

urlpatterns = [
    path('', include(router.urls)),
    #path('becameAssigneeRequest/', views.BecomeAssigneeRequestView.as_view())
#    path('login/', views.login),
#    path('logout/', views.logout)
]
