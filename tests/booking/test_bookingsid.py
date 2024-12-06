import requests
from pytest_check import check

from http import HTTPStatus

def test_getBookingsId(env_config_booking_url):
    respons: requests.Response = requests.get(url=env_config_booking_url)
    response_data=respons.json()
    print("Bookings")
    with check:
        print("Bookings")
        assert respons.status_code==200

    with check:
        assert "bookingid" in response_data[0]



