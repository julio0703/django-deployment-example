from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create/$',views.CreateTaskView.as_view(),name='create'),
    url(r'^task/(?P<pk>\d+)/edit/$',views.UpdateTaskView.as_view(),name='edit'),
    url(r'^$',views.TaskListView.as_view(),name='task_list'),
]
