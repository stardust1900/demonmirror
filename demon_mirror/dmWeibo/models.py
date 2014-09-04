from django.db import models

# Create your models here.
class DemonMirror(models.Model):
	uid = models.CharField(max_length=140,primary_key=True)
	access_token = models.CharField(max_length=140)
	expires_in = models.CharField(max_length=140)