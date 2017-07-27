from rest_framework import serializers
from task_app.models import Tasks

class TaskSerializer(serializers.ModelSerializer):
	deadline = serializers.DateTimeField(format="%d %b, %Y",
										 input_formats=["%d %b, %Y",])
	class Meta:
		fields = ('name', 'status', 'complete_by',
				  'added_on', 'deadline', 'user', 'id')
		model = Tasks