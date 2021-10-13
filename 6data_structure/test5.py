dict1 = {
    "name" : "Zwe Linn Htet",
    "age" : 23,
    "phone" : "09766109458",
    "email" : "zwelinux@gmail.com"
}

print(dict1["name"])
print(dict1["age"])

dict1["name"] = "Ko Zwe Linn Htet"
print(dict1["name"])

dict1.pop("age")
print(dict1)

dict1["fav_food"] = "dark chocolate"
print(dict1)