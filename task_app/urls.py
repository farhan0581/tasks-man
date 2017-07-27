from django.conf.urls import url
from task_app.views import *

urlpatterns = [

    url(r'^tasks$', TasksView.as_view()),
    url(r'^tasks/([0-9]*)/', TasksView.as_view()),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^signup/$', SignupView.as_view(), name='signup'),
    url(r'^task_list/$', TasksListView.as_view(), name='task_list'),
    url(r'^add/$', TaskAddView.as_view(), name='add'),

    ]