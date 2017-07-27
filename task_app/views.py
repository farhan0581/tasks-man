# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from task_app.serializers import TaskSerializer
from task_app.models import Tasks, UserProfile, Activity
from rest_framework import status
from rest_framework.response import Response
from task_app.forms import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class TasksListView(APIView):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TasksListView, self).dispatch(*args, **kwargs)

    def post(self, request):
        data = request.POST
        delete_list = data.getlist('delete')
        status_list = data.getlist('status')
        for elem in delete_list:
            if elem != '':
                Tasks.deletetask(elem, request.user)

        for elem in status_list:
            if elem not in ['', '0']:
                status, id = elem.split("_")
                Tasks.updatestatus(id, status, request.user)

        return redirect('task_list')

    def get(self, request):
        order_by = request.GET.get('order_by')
        queryset = Tasks.getallobjs(request.user, order_by)
        serializer = TaskSerializer(queryset, many=True)
        return render(request, 'tasks_list.html', {'tasks': serializer.data})


class TaskAddView(APIView):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TaskAddView, self).dispatch(*args, **kwargs)

    def post(self, request):
        form = TaskAddForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            deadline = form.cleaned_data['deadline']
            obj = Tasks.addtask(name, deadline, request.user)

        return render(request, 'tasks_add.html', {'form': form})

    def get(self, request):
        form = TaskAddForm
        return render(request, 'tasks_add.html', {'form': form})


class TasksView(APIView):
    def post(self, request):
        data = TaskSerializer(data=request.POST)
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_201_CREATED)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request, user_id=None):
        if not user_id:
            user_id = request.user
        queryset = Tasks.getallobjs(user_id)
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def delete(self, request, user_id, id, format=None):
        if not user_id:
            user_id = request.user
        task = Tasks.getobject(id, user_id)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class LoginView(APIView):
    def post(self, request):
        form = UserLoginForm(request.POST)
        print form
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print email, password
            user = form.authenticate_using_email()
            print user
            if user is not None:
                login(request, user)
                return render(request, 'login.html', {'user': user})
            else:
                return HttpResponse('Invalid Credentials!!!')
        else:
            return HttpResponse('inva')


    def get(self, request):
        form = UserLoginForm()
        return render(request, 'login.html', {'form': form,
                                              'user': request.user})


class LogoutView(APIView):
    def get(self, request):
        logout(request)
        form = UserLoginForm()
        return render(request, 'login.html', {'form': form,
                                              'user': request.user})


class SignupView(APIView):
    def post(self, request):
        form = UserProfileForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            cpassword = form.cleaned_data['confirm_password']
            username = form.cleaned_data['username']
            if password == cpassword:
                x = User.objects.create_user(username, email, password)
                print x
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return render(request, 'signup.html', {'user': user})
            else:
                return HttpResponse('Error')

    def get(self, request):
        form = UserProfileForm()
        return render(request, 'signup.html', {'form': form,
                                               'user': request.user})


class ActivityView(APIView):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ActivityView, self).dispatch(*args, **kwargs)

    def get(self, request):
        qs = Activity.getobjs(request.user)
        return render(request, 'activity.html', {'activity': qs})

