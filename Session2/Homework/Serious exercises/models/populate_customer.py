from models.customer import Customer
from faker import Faker
from random import randint, choice
from configs.database import connect

connect()
fake = Faker()

def khoi_tao():
    for i in range(50):
        custommer = Customer(
            name = fake.name(),
            gender = randint(0,1),
            email = "{0}@gmail.com".format(randint(0,9999)),
            phone_number = fake.phone_number(),
            company = fake.company(),
            contacted = randint(0,1)
        )
        print(i)
        custommer.save()