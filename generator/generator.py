from data.data import Person
from faker import Faker
import random

faker_en = Faker('En')
def generated_person():
    return Person(
        first_name = faker_en.first_name(),
        last_name = faker_en.last_name(),
        current_address = faker_en.address(),
        email=faker_en.email(),
        mobile = faker_en.msisdh(),
        subject='English'
    )

def generated_file():
    path = rF'C:\Users\opliukhin\PycharmProjects\pythonProject\text{random.randint(10,100)}.txt'
    file = open(path,'w')
    file.write(f"HelloWorld{random.randint(10,1000)}")
