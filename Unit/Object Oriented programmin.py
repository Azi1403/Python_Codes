# #oop
# # object = class()
# number = int (12) #number az class adad sahih hast ke meghdarsh 12 ast
# name = str("ali")
# ilia = Person() #in class person o bayad tarif konim ya animal
# zebra = Animal ()


# # object = class()

class student:
    def __init__(self,name,last_name,studentNo,phone,age,units,major):
        self.name = name
        self.last_name = last_name
        self.studentNo = studentNo
        self.phone = phone
        self.age = age
        self.units = units
        self.major = major
        print("hello :))")
        
jamal = student ("jamal","jamali",40371781902,"09356678134",45,[],"Mecanical Engineering")
maryam = student ("maryam","rezaei",40266781902,"09036678134",20,["riazi1"],"Chemistry")


print(jamal.last_name)
print(jamal.major)
print(maryam.phone)



