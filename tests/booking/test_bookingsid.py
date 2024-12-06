import pytest
import requests
from pytest_check import check
from src.models.bookings import Booking, BookingDates, BookingWithId
import pprint

@pytest.mark.wip
def test_get_all_booking_ids(booking_url):
    response: requests.Response = requests.get(url=booking_url)

    with check:
        assert response.status_code == 200

    with check:
        assert len(response.json()) > 0

    with check:
        assert "bookingid" in response.json()[0]

    with check:
        assert isinstance(response.json()[0]["bookingid"], int)


@pytest.mark.skip("Not working")
def test_get_booking_by_id(booking_url, single_booking_with_id):
    response: requests.Response = requests.get(url=f"{booking_url}/{single_booking_with_id.bookingid}")
    booking = Booking.model_validate(response.json())

    with check:
        assert single_booking_with_id.booking == booking
    with check:
        response.status_code == 200

    print(single_booking_with_id)
