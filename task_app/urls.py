from django.conf.urls import url
from task_app.views import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken import views

urlpatterns = [

    url(r'^tasks$', csrf_exempt(TasksView.as_view())),
    url(r'^tasks/([0-9]*)/$', csrf_exempt(TasksView.as_view())),
    url(r'^tasks/([0-9]*)/([0-9]*)/$', csrf_exempt(TasksView.as_view())),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^signup/$', SignupView.as_view(), name='signup'),
    url(r'^task_list/$', TasksListView.as_view(), name='task_list'),
    url(r'^add/$', TaskAddView.as_view(), name='add'),
    url(r'^activity/$', ActivityView.as_view(), name='activity'),
    url(r'^get_auth_token/', views.obtain_auth_token),

    ]