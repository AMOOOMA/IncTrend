from django.db import models


# Message model for testing purposes
class Message(models.Model):
    type = models.CharField(max_length=10)
    body = models.CharField(max_length=50)

    def __str__(self):
        return self.type + ":" + self.body


# Company model
class Company(models.Model):
    name = models.CharField(max_length=10)

    @classmethod
    def create(cls, name):
        company = cls(name=name)
        return company

    def __str__(self):
        return self.name


# model for storing message and its prediction
class Entry(models.Model):
    fetched_date = models.DateField()
    message = models.CharField(max_length=200)
    prediction = models.CharField(max_length=10)
    parent_company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.fetched_date + " " + self.prediction + ":" + self.message
