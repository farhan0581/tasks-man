# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework.views import APIView
from task_app.serializers import TaskSerializer
from task_app.models import Tasks, UserProfile
from rest_framework import status
from rest_framework.response import Response
from task_app.forms import *


class TasksView(APIView):
    def post(self, request):
        data = TaskSerializer(data=request.POST)
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_201_CREATED)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request):
        queryset = Tasks.getallobjs()
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def delete(self, request, id, format=None):
        task = Tasks.getobject(id)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class LoginView(APIView):
    def post(self, request):
        form = UserProfileForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            cpassword = form.cleaned_data['confirm_password']
            username = form.cleaned_data['user_name']
            if password == cpassword:
                UserProfile(user_name=username, email=email,
                            password=password).save()

            else:
                pass

    def get(self, request):
        form = UserProfileForm()
        return render(request, 'login.html', {'form': form})

class LogoutView(APIView):
    pass

class SignupView(APIView):
    pass