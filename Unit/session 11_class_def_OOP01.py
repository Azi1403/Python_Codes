
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
      try:
        file = open("messages.csv", "r")
        messages = file.readlines()
        for line in messages:
            if line.split(",")[1] == self.name:
              print(line)
      except FileNotFoundError:
        print("No messages yet.")


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
         return f"hello {self.name} {self.last_name} "

    def choose(self, unit):
        self.units.append(unit)

    def send_message(self, reciever, message):
        print(f"you can send message to: {Manager.managers_list}")
        reciever = input("enter reciever:")
        message = input("enter message:")
        file = open("messages.csv", "a")
        file.write(f"{self.name},{reciever},{message}\n")
        file.close()
        print("message sent...")


jamal = Student("jamal", "jamali", 40371781902, "09356678134", 45, [], "Mecanical Engineering")
maryam = Student("maryam", "rezaei", 40266781902, "09036678134", 20, ["riazi1"], "Chemistry")
majid = Manager('majid', 'samiei', 88, 'computer', 'php')
ahmad = Manager('ahmad', 'kazemi', 67, 'amoozesh', 'master')

maryam.choose("ordibehesht2")

maryam.send_message('Majid', 'good luck!')
jamal.send_message('Ahmad', 'eteraz be nomreh')

print(majid.managers_list)
print(maryam.units)
print(jamal.last_name)
print(jamal.major)
print(maryam.phone)
print(jamal.hello())