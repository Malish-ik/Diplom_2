import pytest
import requests
from data import Urls
from user_data import generate_user_data


@pytest.fixture()
def create_user_and_get_token():
    payload = generate_user_data()
    requests.post(f'{Urls.main_url}{Urls.api_create_user}', data=payload)
    del payload['name']
    response = requests.post(f'{Urls.main_url}{Urls.api_login_user}', data=payload)
    token = response.json()['accessToken']
    yield token
    requests.delete(f'{Urls.main_url}{Urls.api_delete_user}', headers={'Authorization':token})


@pytest.fixture()
def get_ingredient_hash():
    response = requests.get(f'{Urls.main_url}{Urls.api_get_ingredients}')
    ingredients = response.json()
    return ingredients


