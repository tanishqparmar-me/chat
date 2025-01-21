from django.db import models

class message(models.Model):
    user = models.CharField(max_length=20)
    text = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.user}: {self.text}"
