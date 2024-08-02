import requests
import allure
from data import Urls, ErrorMessage
from user_data import generate_user_data


class TestUser:

    @allure.title('Проверка успешной регистрации нового пользователя')
    @allure.description('Создаем пользователя, проверяем, что код ответа: 200,\
                        и в тексте ответа содержится accessToken')
    def test_create_user(self):
        payload = generate_user_data()
        response = requests.post(f'{Urls.main_url}{Urls.api_create_user}', data=payload)
        token = response.json()['accessToken']
        requests.delete(f'{Urls.main_url}{Urls.api_delete_user}', headers={'Authorization': token})
        assert response.status_code == 200 and 'accessToken' in response.text, (f'Ожидалось 200, получили {response.status_code}, \
                                                                                 ожидалось "accessToken", получили {response.text}')

    @allure.title('Проверка повторной регистрации пользователя, который уже зарегистрирован')
    @allure.description('Создаем пользователя с данными ранее зарегистрированного пользователя, \
    проверяем, что код ответа: 403, и текст ответа "User already exists"')
    def test_create_the_same_user(self):
        payload = generate_user_data()
        requests.post(f'{Urls.main_url}{Urls.api_create_user}', data=payload)
        response = requests.post(f'{Urls.main_url}{Urls.api_create_user}', data=payload)
        assert 403 == response.status_code and  response.json()['message'] == ErrorMessage.text_create_403_double

    @allure.title('Проверка регистрации пользователя с пустым полем e-mail')
    @allure.description('Создаем пользователя с пустым полем e-mail, \
        проверяем, что код ответа: 403, и текст ответа "Email, password and name are required fields"')
    def test_create_user_without_email(self):
        payload = generate_user_data()
        del payload['email']
        response = requests.post(f'{Urls.main_url}{Urls.api_create_user}', data=payload)
        assert 403 == response.status_code and response.json()['message'] == ErrorMessage.text_create_403_wrong


