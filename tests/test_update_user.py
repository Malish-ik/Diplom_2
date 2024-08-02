import pytest
import requests
import allure
from data import Data, Urls, ErrorMessage



class TestUpdateUser:
    @allure.title(
        'Проверка успешного изменения данных пользователя с авторизацией')
    @allure.description('Создаем пользователя, получаем данные пользователя, изменяем name/email, отправляем \
                              запрос на изменение данных с токеном, проверяем, что в ответе приходит статус-код\
                               200 и {"success}: True')
    @pytest.mark.parametrize('update_argument, update_data', (['name', Data.login], ['email', Data.email]))
    def test_update_user_data_success(self, create_user_and_get_token, update_argument, update_data):
        user_data = requests.get(f'{Urls.main_url}{Urls.api_get_user}',
                                 headers={'Authorization': create_user_and_get_token})
        user_data.json()['user'][update_argument] = update_data
        update_user = requests.patch(f'{Urls.main_url}{Urls.api_get_user}', data=user_data,
                                     headers={'Authorization': create_user_and_get_token})
        assert update_user.status_code == 200 and update_user.json()['success'] == True

    @allure.title('Проверка невозможности изменения данных пользователя без авторизации')
    @allure.description('Создаем пользователя, получаем данные пользователя, меняем имя, отправляем \
                          запрос на изменение данных без токена, проверяем, что в ответе приходит ошибка\
                           401 и текст "You should be authorised"')
    def test_update_user_data_no_auth_faild(self, create_user_and_get_token):
        user_data = requests.get(f'{Urls.main_url}{Urls.api_get_user}',
                                 headers={'Authorization': create_user_and_get_token})
        user_data.json()['user']['name'] = Data.login
        update_user = requests.patch(f'{Urls.main_url}{Urls.api_get_user}', data=user_data)
        assert update_user.status_code == 401 and update_user.json()['message'] == ErrorMessage.text_update_401

