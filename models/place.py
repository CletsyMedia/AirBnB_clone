#!/usr/bin/python3
"""Defines the Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represent a place.

    Attributes:
        city_id (str): The City id.
        user_id (str): The User id.
        name (str): The name of the place.
        description (str): The description of the place.
        number_rooms (int): The number of rooms.
        number_bathrooms (int): The number of bathrooms.
        max_guest (int): The maximum number of guests.
        price_by_night (int): The price per night.
        latitude (float): The latitude coordinates.
        longitude (float): The longitude coordinates.
        amenity_ids (list): A list of Amenity ids.
    """
    __slots__ = ["city_id", "user_id", "name", "description", "number_rooms",
                 "number_bathrooms", "max_guest", "price_by_night", "latitude",
                 "longitude", "amenity_ids"]

    def __init__(self, *args, **kwargs):
        """Initialize Place instance."""
        super().__init__(*args, **kwargs)

        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []
