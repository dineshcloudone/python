customer = {
    "name": "abc",
    "age" : 30,
    "is_verified" : "True"
}

print(customer["name"])
#print(customer["Name"]) #throws KeyError
print(customer.get("Name")) #it will not throw error and returns None object
print(customer.get("birhtdate", "Jan 1 1990")) # if birthdate is not there then we can give value

customer["birthdate"] ="Jan 1 1990" # adding new value

print(customer)