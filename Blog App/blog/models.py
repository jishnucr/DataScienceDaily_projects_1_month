from django.db import models

# Create your models here.
class webdata(models.Model):
    title=models.CharField(max_length=50,null=True)
    content=models.TextField(null=True)
    created_date=models.DateTimeField(auto_now=True)
    updated_date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title