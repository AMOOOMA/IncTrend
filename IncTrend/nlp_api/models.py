from django.db import models
from datetime import datetime


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
    fetched_date = models.DateTimeField()
    message = models.CharField(max_length=200)
    prediction = models.CharField(max_length=10)
    parent_company = models.ForeignKey(Company, on_delete=models.CASCADE)

    @classmethod
    def create(cls, message, prediction, company):
        entry = cls(message=message, prediction=prediction, parent_company=company)
        entry.fetched_date = datetime.now()
        return entry

    def __str__(self):
        return self.fetched_date.strftime("%m/%d/%Y, %H:%M:%S") + " " + self.prediction + ":" + self.message
