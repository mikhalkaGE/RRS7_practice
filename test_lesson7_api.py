import pytest
import requests

BASE_URL = 'https://restful-booker.herokuapp.com/booking'
AUTH_URL = 'https://restful-booker.herokuapp.com/auth'
STATUS_OK = 200

@pytest.fixture()
def get_auth_token():
    payload = {
        'username': 'admin',
        'password': 'password123'
    }
    response = requests.post(f'{AUTH_URL}', json=payload)
    auth_tkn = response.json()['token']
    yield auth_tkn

@pytest.fixture()
def get_booking_id():
    payload = {
    "firstname" : "Malhaz",
    "lastname" : "Dolidze",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
    }
    response = requests.post(BASE_URL, json=payload)
    booking_id = response.json()['bookingid']
    yield booking_id


def test_get_all_bookings():
    response = requests.get(BASE_URL)
    assert response.status_code == STATUS_OK, f'Expected 200, but got {response.status_code}'
    assert 'Connection' in response.headers, 'There is no Connection key in the headers'
    # print(response.headers)
    # print(response.json())

def test_get_booking_by_id():
    response = requests.get(f'{BASE_URL}/1')
    response_data = response.json()
    # assert response_data['firstname'] == 'Mark'

    expected_keys = ['firstname', 'lastname', 'totalprice', 'depositpaid', 'bookingdates']
    for key in expected_keys:
        assert key in response_data.keys()

    assert response.status_code == STATUS_OK, f'Expected 200, but got {response.status_code}'
    
    print(response_data)

def test_create_booking():
    payload = {
    "firstname" : "Malhaz",
    "lastname" : "Dolidze",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"}
    
    response = requests.post(BASE_URL, json=payload)
    assert response.status_code == STATUS_OK, f'Expected 200, but got {response.status_code}'
    print(response.json())

    booking_id = response.json()['bookingid']
    get_response = requests.get(f'{BASE_URL}/{booking_id}')
    print(f'\n {get_response.json()}')
    assert get_response.json()['firstname'] == 'Malhaz', f"Expected firstname Malhaz, but got {get_response.json()['firstname']}"

def test_create_booking_with_fixture(get_booking_id):
    get_response = requests.get(f'{BASE_URL}/{get_booking_id}')
    assert get_response.json()['firstname'] == 'Malhaz', f"Expected firstname Malhaz, but got {get_response.json()['firstname']}"

def test_show_auth_token(get_auth_token):
    print(f'\nAUTH TOKEN: {get_auth_token}')

def test_delete_booking(get_booking_id, get_auth_token):
    headers = {
        'Cookie': f'token={get_auth_token}'
    }
    delete_response = requests.delete(f'{BASE_URL}/{get_booking_id}', headers=headers)
    assert delete_response.status_code == 201
