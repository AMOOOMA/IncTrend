from django.db import models


# Message model for testing purposes
class Message(models.Model):
    type = models.CharField(max_length=10)
    body = models.CharField(max_length=50)

    def __str__(self):
        return self.type + ":" + self.body

