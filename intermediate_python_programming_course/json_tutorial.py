import json

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

# convert from python dictionary to json/json file
personJSON = json.dumps(person, indent=4, sort_keys=True)
print(personJSON)

with open("person.json", "w") as file:
    json.dump(person, file, indent=4)

# convert from json to python string
person = json.loads(personJSON)
print(person)

with open("person.json", "r") as file:
    person = json.loads(personJSON)
    print(person)

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User("Matt", 27)

def encode_user(o):
    if isinstance(o, User):
        return {"name": o.name, "age": o.age, o.__class__.__name__: True}
    else:
        raise TypeError("Object of type User is not JSON serializable")

from json import JSONEncoder
class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {"name": o.name, "age": o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)

# userJSON = json.dumps(user, cls=UserEncoder)
userJSON = json.dumps(user, default=encode_user)
print(userJSON)