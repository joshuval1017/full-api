from django.db import models
from django.contrib.auth.models import User



class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=26)
    file =  models.ImageField(upload_to='user_images/', null=True, blank=True)  
    create = models.DateField(auto_now_add=True)

    
