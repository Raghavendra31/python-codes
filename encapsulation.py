# encapsulation is the process of hiding the internal state and functionality of an object
# and only exposing a controlled interface to the outside world.

# encaplsualtion is the proess of wrapping the attributes and methods of an object


class db:
    def __init__(self):
        self.__storage = {}

    def write(self,key,value):
        self.__storage[key] =value
    
    def read(self,key):
        if key in self.__storage:
            return self.__storage[key]
        else:
            return "Key not found"


r = db()
r.write("name", "John Doe")
print(r.read("ragu"))