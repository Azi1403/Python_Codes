class Manager:
    managers_list = []

    def __init__(self, name, last_name, age, faculty, degree):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.faculty = faculty
        self.degree = degree
        Manager.managers_list.append(name)

    def show_messages(self):
        file = open("messages.csv", "r")
        messages = file.readlines()
        for line in messages:
           if line.split(",")[1] == self.name:
             print(line)

class Student:
    def __init__(self, name, last_name, studentNo, phone, age, units, major):
        self.name = name
        self.last_name = last_name
        self.studentNo = studentNo
        self.phone = phone
        self.age = age
        self.units = units
        self.major = major

    def hello(self):
        return f"Hello {self.name} {self.last_name}."

    def choose(self, unit):
        self.units.append(unit)

    def send_message(self, manager_name, message):
        print(f"you can send message to: {Manager.managers_list}")
        reciever = input("Enter reciever: ")
        if reciever.lower() == manager_name.lower():
            message = input("Enter message: ")
            file = open("messages.csv", "a")
            file.write(f"{self.name},{reciever},{message}\n")
            file.close()
            print("Message Sent...")
        else:
            print("Invalid reciever.")

jamal = Student("Jamal", "Jamali", 40371781902, "09123456789", 45, [], "Mechanical Engineering")
maryam = Student("Maryam", "Rezaei", 40261641809, "09218793435", 20, ["Riazi1"], "Chemistry")

majid = Manager("Majid", "Samiei", 88, "Computer", "PHD")
ahmad = Manager("Ahmad", "Kazemi", 67, "Amoozeh", "Master")

print(jamal.hello())
print(maryam.hello())

maryam.choose("andishe2")
print(maryam.units)

maryam.send_message('Majid', 'good luck!')
jamal.send_message('Ahmad', 'eteraz be nomreh')