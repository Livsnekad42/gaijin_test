from django.db import models


class Player(models.Model):
    username = models.CharField(max_length=80)
    score = models.IntegerField(blank=True, null=True)
    avatar = models.ImageField(upload_to="profiles/avatars", null=True, blank=True)

    
