from django.contrib import admin
from django.urls import path
from .views import TaskCreateView,TaskListView,TaskDetails,TaskUpdate,DeleteTaskView,search,filter

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('tasklist/',TaskListView.as_view(),name='tasklist'),
    path('search/',search,name="search"),
    path('filter/',filter,name="filter"),
    path('taskcreate/',TaskCreateView.as_view(),name='taskcreate'),
    path('edittask/<int:pk>/',TaskUpdate.as_view(),name='edittask'),
    path('deletetask/<int:pk>/',DeleteTaskView.as_view(),name='deletetask'),
    path('taskdetail/<int:id>',TaskDetails.as_view(),name='taskdetail'),
]
