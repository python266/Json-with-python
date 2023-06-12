import json
from json import JSONEncoder
class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price
#class Vehicle_S(JSONEncoder):
#    def default(self, o):
#        return o.__dict__

vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)

# Convert it into JSON format
data = json.dumps(vehicle.__dict__, indent=2)
print(data)