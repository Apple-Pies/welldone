from django.db import models

class Task(models.Model):

	MyCHOICES = (
			('Least Important', '✨ Least Important'),
			('Somewhat Important', '⭐ Somewhat Important'),
			('Mandatory', '🌟 Mandatory'),
			)
	
	name = models.CharField(max_length=200)
	note = models.CharField(max_length=800)
	completion = models.BooleanField(default=False)
	priority = models.CharField(max_length=200, null=True, choices=MyCHOICES)
	Time_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name
