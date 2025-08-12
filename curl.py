
class Url:
    MAIN_URL = 'https://stellarburgers.nomoreparties.site'
    CREATE_USER = '/api/auth/register'
    LOGIN_USER = '/api/auth/login'
    CREATE_ORDER = '/api/orders'
    GET_INGREDIENTS = '/api/ingredients'

    @classmethod
    def create_user_url(cls):
        return f'{cls.MAIN_URL}{cls.CREATE_USER}'

    @classmethod
    def login_user_url(cls):
        return f'{cls.MAIN_URL}{cls.LOGIN_USER}'

    @classmethod
    def create_order_url(cls):
        return f'{cls.MAIN_URL}{cls.CREATE_ORDER}'

    @classmethod
    def get_ingredient_url(cls):
        return f'{cls.MAIN_URL}{cls.GET_INGREDIENTS}'
