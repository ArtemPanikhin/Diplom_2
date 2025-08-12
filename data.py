import generators

INGREDIENT_ERROR = 'Ingredient ids must be provided'
USER_EXIST_ERROR = 'User already exists'
REQUIRED_FIELDS_ERROR = 'Email, password and name are required fields'
INCORRECT_DATA_ERROR = 'email or password are incorrect'

class DataForRegistration:
    reg_data = [
        {
            'login': generators.email_generator(), 'name': generators.name_generator()
        },
        {
            'password': generators.password_generator(), 'name': generators.name_generator()
        }
    ]

class AuthorizationData:
    create_body = {
        "email" : "imail@imail.com",
        "password" : "password"
    }

class RandomAutorizationData:
    aut_data = [
        {
            'login': generators.email_generator(), 'password': ''
        },
        {
            'login': '', 'password': generators.password_generator()
        }
    ]
