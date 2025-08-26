'''ragu = {

    "keys":"value"

}'''

# date = {
#     "ragu":"15/7/2005",
#     "mallika":"20/1/1984"
# }

# print (date["ragu"])
# print (date ["mallika"])

# # know about get keyword

# print(date.get("ronaldo", "couldn't find"))

# item1={
#     "name":"milk",
#     "weight":1
# }

# item2 = {
#     "name":"sugar",
#     "weight":2
# }

# items=[ item1,item2,]
# print (items)
# print (f'total weigth = {item1["weight"] + item2 ["weight"] }kg')


# d = {"bengaluru": "vade",
#      "mumbai": "vada pav",
#      "chennai": "idli",
#      "delhi": "chole bhature"}

# d.update({"hyderabad": "biryani"})  # Adding a new key-value pair

# d.pop("mumbai")
# # i want to change the dish of bengaluru to dosa
# d["bengaluru"] = "dosa"
# # using the key() method to get all keys
# key = d.values()
# print(key)


# nested dictionary example

# n = {"friend 1" : {"name": "Raghavendra", "age": 30, "city": "Bangalore"},
#         "friend 2": {"name": "Mallika", "age": 29, "city": "Chennai"},
#         "friend 3": {"name": "Kumar", "age": 32, "city": "Hyderabad"}}

# for friend, details in n.items():
#      print(f"{friend}:")
#      for key, value in details.items():
#          print(f"  {key}: {value}")
#      print()  # Print a newline for better readability
# print(f"city of friend 1 is {n['friend 2']['city']}")

d = {"bru": 1,
     "nescafe": 2,
     "tata": 3,
     "coffee day": 4}

for key, value in d.items():
    #sum of all values
    print (value)
    total = sum(d.values())
print (total)

#dictionaries are the collection of key and values 
