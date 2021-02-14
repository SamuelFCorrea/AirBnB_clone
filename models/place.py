#!/usr/bin/python3

'''Class State inherit from BaseModel'''
import datetime
from models.base_model import BaseModel
from models import storage


class Place(BaseModel):
    '''A Place class to save a state information'''

    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = int
    number_bathrooms = int
    max_guest = int
    price_by_night = int
    latitude = float
    longitude = float
    amenity_ids = []

    def __init__(self, *args, **kargs):
        '''Initialize the class with the respective passed
values or the kargs ones'''

        if kargs is None or len(kargs) < 1:
            super().__init__()
        else:
            for key, value in kargs.items():
                if key == '__class__':
                    continue
                elif key in {'updated_at', 'created_at'}:
                    setattr(self, key, datetime.datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)
        storage.new(self)
