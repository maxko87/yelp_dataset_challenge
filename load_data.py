'''
Loads data from json objects into python objects.
Parameters:
    number - the number of objects to load.
'''
from objects import User, Business, Checkin, Review
import json

data_path = "data/"

def load_object(object_name, number=-1):
    object_path = data_path + object_name + ".json"
    f = open(object_path)
    all_objects = []
    i = 0
    for line in f.readlines():
        object_json = json.loads(line)

        if object_name == "user":
            this_object = User()
        elif object_name == "business":
            this_object = Business()
        elif object_name == "checkin":
            this_object = Checkin()
        elif object_name == "review":
            this_object = Review()

        for param in object_json:
            setattr(this_object, param, object_json[param])     
        all_objects += [this_object]
        if i == number:
            break
    return all_objects



businesses = load_object("business", 100)
print businesses