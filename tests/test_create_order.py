import requests
import allure
from data import Data, Urls, ErrorMessage, Burgers

class TestCreateOrder:

    @allure.title('Проверка создания заказа с авторизацией')
    @allure.description('Создаем пользователя, автриизуемся, создаем заказ, проверяем, что в ответе "success: True",\
                        и name заказа соответствует заказанным ингредиентам')
    def test_create_order_with_auth(self, create_user_and_get_token, get_ingredient_hash):
        requests.post(f'{Urls.main_url}{Urls.api_login_user}', data=create_user_and_get_token)
        ingredients = {'ingredients': [get_ingredient_hash['data'][0]['_id'], get_ingredient_hash['data'][2]['_id'], get_ingredient_hash['data'][7]['_id']]}
        response = requests.post(f'{Urls.main_url}{Urls.api_create_order}', data=ingredients)
        order = response.json()
        assert order['name'] == Burgers.met_flu_classic and order['success'] == True

    @allure.title('Проверка создания заказа без авторизации')
    @allure.description('Создаем заказ, проверяем, что в ответе "success: True",\
                            и name заказа соответствует заказанным ингредиентам')
    def test_create_order_wihtout_auth(self, get_ingredient_hash):
        ingredients = {'ingredients': [get_ingredient_hash['data'][1]['_id'], get_ingredient_hash['data'][3]['_id'], get_ingredient_hash['data'][6]['_id']]}
        response = requests.post(f'{Urls.main_url}{Urls.api_create_order}', data=ingredients)
        order = response.json()
        assert order['name'] == Burgers.space_mars and order['success'] == True

    @allure.title('Проверка создания заказа без ингредиентов')
    @allure.description('Создаем заказ без ингредиентов, проверяем, что код ответа 400,\
                                и текст ответа "Ingredient ids must be provided"')
    def test_create_order_without_ingredients(self, get_ingredient_hash):
        ingredients = {'ingredients': []}
        response = requests.post(f'{Urls.main_url}{Urls.api_create_order}', data=ingredients)
        assert response.status_code == 400 and response.json()['message'] == ErrorMessage.text_order_without_ingredients

    @allure.title('Проверка создания заказа c ингредиентами')
    @allure.description('Создаем заказ с ингредиентами, проверяем, что в ответе "success: True",\
                            и name заказа соответствует заказанным ингредиентам')
    def test_create_order_with_ingredients(self, create_user_and_get_token, get_ingredient_hash):
        ingredients = {'ingredients': [get_ingredient_hash['data'][1]['_id'], get_ingredient_hash['data'][4]['_id'], get_ingredient_hash['data'][8]['_id']]}
        response = requests.post(f'{Urls.main_url}{Urls.api_create_order}', data=ingredients)
        order = response.json()
        assert order['name'] == Burgers.spicy and order['success'] == True

    @allure.title('Проверка создания заказа c неверным хэш ингредиентов')
    @allure.description('Создаем заказ передавая неверный хэш ингредиента, проверяем, что код ответа 500')
    def test_create_order_with_unvalid_hash_ingredients(self, get_ingredient_hash):
        ingredients = {'ingredients': [Data.f_hash, Data.f_hash]}
        response = requests.post(f'{Urls.main_url}{Urls.api_create_order}', data=ingredients)
        assert response.status_code == 500








