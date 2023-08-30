from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    user =models.ForeignKey(User, on_deLete=models.CASCADE,null =True, bLank=True)
    title = models.CharField(max_Length=200)
    description =models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.title
    
    class Meta:
        ordering = ['complete']

