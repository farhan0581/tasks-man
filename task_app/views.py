# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework.views import APIView
from task_app.serializers import TaskSerializer
from task_app.models import Tasks
from rest_framework import status
from rest_framework.response import Response


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
        snippet = Tasks.getobject(id)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)