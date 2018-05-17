from configs.db_config import connect
from models.service import Service
from faker import Faker
from random import randint, choice

def populate():
    connect()
    fake = Faker()
    for i in range(100):
        service = Service(
            name = fake.name(),
            yob = randint(1980,2001),
            height = randint(150,190),
            phone = fake.phone_number(),
            address = fake.address(),
            image = "https://via.placeholder.com/300x200",
            description = fake.text(),
            measurements = [
                randint(40,90), 
                randint(35,100), 
                randint(45,150)]
        )
        service.save()
        print(i)