from django.conf.urls import url
from task_app.views import *

urlpatterns = [

    url(r'^tasks$', TasksView.as_view()),
    url(r'^tasks/([0-9]*)/', TasksView.as_view()),

    ]