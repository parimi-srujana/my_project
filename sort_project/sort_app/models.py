from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()  # Use IntegerField for numeric values

    def __str__(self):
        return self.name  # Returns the name when the object is printed
