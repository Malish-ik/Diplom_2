from faker import Faker
from random import randint

class Data:
    Faker.seed(randint(1000, 10000))
    faker = Faker()
    f_hash = faker.md5(raw_output=False)
    login = faker.name()
    email = faker.email()
class Urls:
    main_url = "https://stellarburgers.nomoreparties.site"
    api_create_user = "/api/auth/register"
    api_login_user = "/api/auth/login"
    api_order = "/api/v1/orders"
    api_delete_user = "/api/auth/user"
    api_get_user = '/api/auth/user'
    api_get_ingredients = "/api/ingredients"
    api_create_order = "/api/orders"
class ErrorMessage:
    text_login_401 = 'email or password are incorrect'
    text_login_404 = "Учетная запись не найдена"
    text_create_403_double = "User already exists"
    text_create_403_wrong = "Email, password and name are required fields"
    text_create_400 = "Недостаточно данных для создания учетной записи"
    text_update_401 = "You should be authorised"
    text_order_without_ingredients = "Ingredient ids must be provided"
    text_get_orders_no_auth = "You should be authorised"

class Burgers:
    met_flu_classic = 'Метеоритный флюоресцентный традиционный-галактический бургер'
    space_mars = 'Space бессмертный био-марсианский бургер'
    spicy = 'Spicy бессмертный краторный бургер'
