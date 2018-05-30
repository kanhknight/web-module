from models.service import Service
from faker import *
from random import randint, choice
import mlab

mlab.connect()

fake = Faker()

for i in range(50):
    service = Service(
        name = fake.name(),
        yob = randint(1990,2001),
        gender = randint(0,1),
        height = randint(150,190),
        phone = fake.phone_number(),
        address = fake.address(),
        status = choice([True, False])
        )
    print(i)
    service.save()