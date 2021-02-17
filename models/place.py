#!/usr/bin/python3

'''
Class State inherit from BaseModel

    Attributes:
        city_id: it will be the City.id
        user_id: it will be the User.id
        name: name
        description: description
        number_rooms: number of rooms
        number_bathrooms: number of bathrooms
        max_guest: max guest
        price_by_night: price by night
        latitude: latitude
        longitude: longitude
        amenity_ids: it will be the list of Amenity.id

    Methods: inherits from BaseModel
'''

import datetime
from models.base_model import BaseModel


class Place(BaseModel):
    '''
    A Place class to save a state information
    '''

    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
