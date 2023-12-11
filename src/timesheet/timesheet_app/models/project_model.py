from django.db import models

class Project(models.Model):
    project_name = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.project_name