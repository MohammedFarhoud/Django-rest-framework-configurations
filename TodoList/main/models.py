from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=40)
    body = models.TextField(max_length=200)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    
    def getBody(self):
        return self.body[:100]+'...'