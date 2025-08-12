'''ragu = {

    "keys":"value"

}'''

date = {
    "ragu":"15/7/2005",
    "mallika":"20/1/1984"
}

print (date["ragu"])
print (date ["mallika"])

# know about get keyword

print(date.get("ronaldo", "couldn't find"))

item1={
    "name":"milk",
    "weight":1
}

item2 = {
    "name":"sugar",
    "weight":2
}

items=[ item1,item2,]
print (items)
print (f'total weigth = {item1["weight"] + item2 ["weight"] }kg')