# models.py
from django.db import models
from django.contrib.auth.models import User

class HintExplanation(models.Model):
    hint_or_explanation_text = models.TextField()
    image = models.ImageField(upload_to='images/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_input = models.TextField()