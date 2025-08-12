from faker import Faker

fake = Faker()

def email_generator():
    generated_email = fake.ascii_free_email()
    return generated_email

def password_generator():
    generated_password = fake.password(length=10)
    return generated_password

def name_generator():
    generated_name = fake.first_name()
    return generated_name

def generate_credentials():
    email = email_generator()
    password = password_generator()
    return email, password

def generate_register_body(user_credentials):
    email, password = user_credentials
    return {
        "email": email,
        "password": password,
        "name": fake.first_name()
    }

def generate_authorization_body(user_credentials_tuple):
    (email, password) = user_credentials_tuple
    return {
        "email": email,
        "password": password
    }

def generate_order_body(hash_ids):
    return {
        "ingredients": hash_ids
    }
