#Object Oriented Programming (OOP)
# object = Class()

class Person:
    def __init__(self,name,last_name,age):
        self.name = name
        self.last_name = last_name
        self.age = age

    def birthday(self):
        print(f"Happy Birthday {self.name}🎈!")
        self.age += 1

    def __str__(self):
        return f"{self.name} {self.last_name}"



class Manager(Person):

    managers_list = []
    
    def __init__(self,name,last_name,age,faculty,degree):
        super().__init__(name,last_name,age)
        self.faculty = faculty
        self.degree = degree
        Manager.managers_list.append(name)
    
    def show_messages(self):
        file = open("messages.csv","r")
        messages = file.readlines()
        for line in messages:
            if line.split(",")[1] == self.name:
                print(line)
    
    def birthday(self):
        print(f"Happy birthday {self.name} {self.last_name} 🎈🎉✨🎇🎁🤑!")
        self.age += 1
 


class Student(Person):
    def __init__(self,name,last_name,studentNo,phone,age,units,major):
        super().__init__(name,last_name,age)
        self.studentNo = studentNo
        self.phone = phone
        self.units = units
        self.major = major
        #print("Hello :))")

    def hello(self):
        return f"Hello {self.name} {self.last_name}."
    
    def choose(self,unit):
        self.units.append(unit)
    
    def send_message(self):
        print(f"you can send message to: {Manager.managers_list}")
        reciever = input("Enter reciever:")
        message = input("Enter message:")
        file = open("messages.csv","a")
        file.write(f"{self.name},{reciever},{message}\n")
        file.close()
        print("Message Sent...")
    
        


jamal = Student("Jamal","Jamali",40371781902,"09123456789",45,[],"Mechanical Engineering")
maryam = Student("Maryam", "Rezaei", 40261641809,"09218793435",20,["Riazi1"],"Chemistry")
majid = Manager("Majid","Samiei",88,"Computer","PHD")
ahmad = Manager("Ahmad","Kazemi",67,"Amoozeh","Master")

print(maryam)
print(jamal)
print(ahmad)
print(majid)

