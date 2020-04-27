from django.db import models

# Create your models here.
class Task(models.Model):
	title = models.TextField(max_length=100)
	completed = models.BooleanField(default=False, blank=True, null=True)
	def __str__(self):
		return self.title + ' | ' +str(self.completed)

class Borrowed(models.Model):
	what = models.ForeignKey(Task, on_delete=models.CASCADE)
