# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.shortcuts import get_object_or_404

class Tasks(models.Model):
	TASK_STATUS = (
			(1, 'Complete'),
			(0, 'Incomplete')
		)
	name = models.TextField()
	status = models.IntegerField(choices=TASK_STATUS, default=0)
	complete_by = models.DateTimeField(blank=True, null=True)
	added_on = models.DateTimeField(auto_now=True)
	deadline = models.DateTimeField()

	class Meta:
		db_table = 'tasks'

	@classmethod
	def getallobjs(cls):
		return cls.objects.all()

	@classmethod
	def getobject(cls, id):
		return get_object_or_404(cls, id=id)

class Activity(models.Model):
	action = models.TextField()
	insert_time = models.DateTimeField(auto_now=True)
	task_name = models.TextField(blank=True, null=True)

	class Meta:
		db_table = 'activity'