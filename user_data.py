from faker import Faker

def generate_user_data():
    fake = Faker()
    payload = {
        "email": fake.email(),
        "password": fake.password(),
        "name": fake.name()
    }
    return payload
