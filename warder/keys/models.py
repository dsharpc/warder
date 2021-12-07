from typing import Match
from django.db import models

class Credential(models.Model):
    site = models.CharField(max_length=100)
    website = models.URLField(blank=True)
    user = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    additional_text = models.TextField(blank=True)
