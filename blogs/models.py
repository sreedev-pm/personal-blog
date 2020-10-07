from django.db import models

# Create your models here.
class blogmodel(models.Models):
    title=models.CharField(max_length="100")
    content=models.TextField()
    Auther=models.Charfield(max_length="20")
    date=models.DateTimeField()
    def __str__(self):
        return self.title