# file = open("data.csv","r") 
# print(file.read())

class Student:
    def __init__(self, name, last_name, studentNo, phone, age, units, major):
        self.name = name
        self.last_name = last_name
        self.studentNo = studentNo
        self.phone = phone
        self.age = age
        self.units = units
        self.major = major

jamal = Student("jamal", "jamali", 40371781902, "09356678134", 45, [], "Mechanical Engineering")
maryam = Student("maryam", "rezaei", 40266781902, "09036678134", 20, ["riazi1"], "Chemistry")



def check_and_add_student(studentNo, file_name):
   with open("data.csv", "r") as file:
    for line in file:
     if str(studentNo) in line:
         return f"StudentNo. {studentNo} already exists."
   with open(file_name, "a") as file:
    file.write(f"{jamal.name},{jamal.last_name},{jamal.studentNo},{jamal.phone},{jamal.age},{jamal.units},{jamal.major}\n")
    file.write(f"{maryam.name},{maryam.last_name},{maryam.studentNo},{maryam.phone},{maryam.age},{maryam.units},{maryam.major}\n")
   return f"Students added to the file successfully."

print(check_and_add_student(jamal.studentNo, "data.csv"))
print(check_and_add_student(maryam.studentNo, "data.csv"))