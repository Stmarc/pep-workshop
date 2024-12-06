import pytest
import requests
from pytest_check import check
from src.models.bookings import Booking, BookingDates, BookingWithId
import pprint


def test_update_partial(booking_url,single_booking_with_id_from_json,fake_names,token):

    url=f"{booking_url}/{single_booking_with_id_from_json.bookingid}"
    headers = {"Cookie": f"token={token}", "Content-Type": "application/json", "Accept":"application/json"}
    response_update=requests.patch(url=url,headers=headers,json=fake_names.model_dump())

    print(response_update.json())
    booking = Booking.model_validate(response_update.json())
    with check:
        assert response_update.status_code==200
    with check:
        assert booking!=single_booking_with_id_from_json.booking

