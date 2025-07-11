# key-value

# frog: قورباغه
# معنی : لغت


information = {"name":"azam",
               "last name":"bayat",
               "age":40,
               "phone":"09356678134"
               }

print(information)

print(information["age"])

#add a key in dic
information["email"] = "azam.b001@gmail.com"
print(information)

#change or edit dic
information['age']=28
print(information)

# del a key in dic
del information["phone"]
print(information)

contacts = {"Dara Mansouri":"09121234567",
            "Sara Mansouri":"09334562277",
            "Ahmad Kazemi":"093012345867",
            "Mahnaz Afshar":"09102345677"
}

print(contacts["Ahmad Kazemi"]) #print phone num Ahmad Kazemi

#Add in dic
#name=input ("Enter Name: ")
#phone = input("Enter phone num: ")
#contacts[name]=phone
#print(contacts)


for item in contacts:
    print(item) #print name=key
    
    
for item in contacts:
    print(contacts[item]) #print phone=value
    
for item in contacts:
    print(item,contacts[item]) #print key and value
    
    
print (contacts.keys())
print (contacts.values())




