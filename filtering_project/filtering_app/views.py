from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Person
from faker import Faker
import random

def person_list(request):
    persons = Person.objects.all()  # ✅ Correct indentation
    return render(request, 'person_list.html', {'persons': persons})

def insert_rows(request):
    fake = Faker()
    for _ in range(5):  # ✅ Correct indentation
        Person.objects.create(
            name=fake.name(),
            age=random.randint(18, 80),
            email=fake.email()
        )
    return HttpResponse("5 records inserted successfully.")

