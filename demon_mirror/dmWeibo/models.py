from django.db import models

# Create your models here.
class DemonMirror(models.Model):
	uid = models.CharField(max_length=140)
	access_token = models.CharField(max_length=140)
	expires_in = models.CharField(max_length=140)