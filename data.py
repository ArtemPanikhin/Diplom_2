import generators



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
