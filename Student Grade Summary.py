name = input("please enter Student's full name: ")
age = eval(input("please enter Age:"))
course_name = input ("please enter Course name:")
a,b,c = map(eval,input("please enter 3 test scores:").split())

print(name.upper())
s=a+b+c
print(f"Average Scores is: {s/3}")

if s/3 >=60:
    print(f"Passed, {True}")
else:
    print(f"Failed, {False}")