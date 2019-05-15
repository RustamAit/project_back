from django.urls import path, include
from rest_framework import routers

from api import views


router = routers.DefaultRouter()
router.register('users', views.UserList)
router.register('experts', views.ExpertList)
router.register('assignees', views.AssigneeList)
router.register('taskList', views.TaskArray)
router.register('BecomeAssigneeRequests',views.BecomeAssigneeRequestView)

urlpatterns = [
    path('', include(router.urls)),
    path('becameAssigneeRequestList/', views.BecomeAssigneeRequestList.as_view()),
    path('login/', views.login_view),
    path('logout/', views.logout_view),
    path('task/crud', views.TaskView.as_view()),
    path('tasks/',views.TaskList.as_view()),
    path('executeTask/', views.addExecutor),
]
