from django.db import models
from django.urls import reverse
# Create your models here.
class ToDo(models.Model):
	content = models.TextField()
	completed = models.BooleanField(default=False, blank=True, null=True)


    #added from youtube
    # def __str__(self):
    #     return self.titel

	def __str__(self):
		return self.content + ' | ' +str(self.completed)
	
	def get_absolute_url(self):
		return reverse('todo_list')