from django.db import models

# Create your models here.
class welcome(models.Model):
    title=models.CharField(max_length=150,blank=False)
    description=models.TextField(max_length=300,blank=False)


    def __str__(self):
        return self.title
    