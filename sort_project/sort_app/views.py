from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
from faker import Faker
import random

def insert_rows(request):
    fake = Faker()
    for _ in range(10):
        Person.objects.create(
            name=fake.name(),
            age=random.randint(18, 80),
            email=fake.email()
        )
    return HttpResponse("10 records inserted successfully.")

def person_list(request):
    sort_by = request.GET.get('sort', '').strip()
    order = request.GET.get('order', 'asc').strip()

    valid_fields = ['name', 'age', 'email']
    if sort_by not in valid_fields:
        sort_by = 'name'  # Default to sorting by name

    if order == "desc":
        sort_by = f"-{sort_by}"  # Django uses "-" for descending order

    persons = Person.objects.all().order_by(sort_by)
    return render(request, 'person_list.html', {'persons': persons, 'sort_by': sort_by, 'order': order})
