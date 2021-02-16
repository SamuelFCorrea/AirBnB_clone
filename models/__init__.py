'''
All the classes needed to the AirBnB clone:

    BaseModel: Assing id and the updated/created time parentclass
               for the other ones
    User: Public class attributes 'email', 'password', 'first_name',
          'last_name'
    State: Public class attributes 'name'
    City: Public class attributes 'state_id', 'name'
    Amenity: Public class attributes 'name'
    Place: Public class attributes 'city_id', 'user_id', 'name', 'description',
           'number_rooms', 'number_bathrooms', 'max_guest', 'price_by_night',
           'latitude', 'longitude', 'amenity_ids'
    Review: Public class attributes 'place_id', 'user_id', 'text'

    One class per file.

    BaseModel Methods:
        save(): save the object and actualice the 'updated_at' date
        to_dict(): return a dictionary with all the object atributtes
                   and the class name

    String Representation Model: [<class name>] (<self.id>) <self.__dict__>
'''

from models.engine.file_storage import FileStorage


storage = FileStorage()

storage.reload()
