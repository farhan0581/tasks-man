# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

class Tasks(models.Model):
	TASK_STATUS = (
			(1, 'Complete'),
			(0, 'Incomplete')
		)
	user = models.ForeignKey(User, on_delete=models.PROTECT,
							 related_name='task_user')
	name = models.TextField()
	status = models.IntegerField(choices=TASK_STATUS, default=0)
	complete_by = models.DateTimeField(blank=True, null=True)
	added_on = models.DateTimeField(auto_now=True)
	deadline = models.DateTimeField()

	class Meta:
		db_table = 'tasks'

	@classmethod
	def getallobjs(cls, user):
		return cls.objects.filter(user=user)

	@classmethod
	def getobject(cls, id, user):
		return get_object_or_404(cls, id=id, user=user)

	@classmethod
	def addtask(cls, name, deadline, user):
		obj = cls(name=name, deadline=deadline, user=user).save()
		return obj


class Activity(models.Model):
	user = models.ForeignKey(User, on_delete=models.PROTECT,
							 related_name='activity_user')
	action = models.TextField()
	insert_time = models.DateTimeField(auto_now=True)
	task_name = models.TextField(blank=True, null=True)

	class Meta:
		db_table = 'activity'


class UserProfile(models.Model):
	user_name = models.CharField(max_length=100)
	email = models.EmailField()
	password = models.CharField(max_length=50)

	class Meta:
		db_table = 'user_profile'