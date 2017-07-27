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
	def getallobjs(cls, user, order_by=None):
		qs = cls.objects.filter(user=user)
		if order_by:
			qs = qs.order_by(order_by)
		return qs

	@classmethod
	def getobject(cls, id, user):
		return get_object_or_404(cls, id=id, user=user)

	@classmethod
	def addtask(cls, name, deadline, user):
		obj = cls(name=name, deadline=deadline, user=user).save()
		try:
			Activity.addactivity(user=user,
								 task_name=name,
								 action='You added this task'
								 )
		except:
			pass
		return obj

	@classmethod
	def deletetask(cls, id, user):
		obj = cls.objects.filter(id=id, user=user)
		name = obj[0].name
		obj.delete()
		try:
			Activity.addactivity(user=user,
								 task_name=name,
								 action='You deleted this task'
								 )
		except Exception as e:
			pass

	@classmethod
	def updatestatus(cls, id, status, user):
		changed = False
		status_verbose = {1: 'Complete', 0: 'Incomplete'}
		obj = cls.objects.filter(id=id, user=user)
		name = obj[0].name

		old_status = obj[0].status
		if int(status) != old_status:
			obj.update(status=status)
			changed = True
		try:
			if changed:
				Activity.addactivity(user=user,
								 	task_name=name,
								 	action='You updated this task\'s status to ' + status_verbose.get(int(status), '')
								 	)
		except Exception as e:
			pass

class Activity(models.Model):
	user = models.ForeignKey(User, on_delete=models.PROTECT,
							 	   related_name='activity_user')
	action = models.TextField()
	insert_time = models.DateTimeField(auto_now=True)
	task_name = models.TextField(blank=True, null=True)

	class Meta:
		db_table = 'activity'

	@classmethod
	def addactivity(cls, **kwargs):
		obj = cls(**kwargs).save()
		return obj

	@classmethod
	def getobjs(cls, user):
		qs = cls.objects.filter(user=user)
		return qs


class UserProfile(models.Model):
	user_name = models.CharField(max_length=100)
	email = models.EmailField()
	password = models.CharField(max_length=50)

	class Meta:
		db_table = 'user_profile'