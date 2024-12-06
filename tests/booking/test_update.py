import pytest
import requests
from pytest_check import check
from src.models.bookings import Booking, BookingDates, BookingWithId
import pprint


def test_update(booking_url,token,single_booking_with_id_from_json):

    url = f"{booking_url}/{single_booking_with_id_from_json.bookingid}"

    headers = {"Cookie": f"token={token}", "Content-Type": "application/json"}
    response_delete = requests.delete(url=url, headers=headers)


    with check:
        response_delete.status_code==201

    url_check=f"{booking_url}/{single_booking_with_id_from_json.bookingid}"
    response_check=requests.get(url=url_check)
    print(response_check.status_code)

    with check:
        response_check.status_code==404



