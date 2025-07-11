import requests

birthdate = input("Enter birthdate:")

response = requests.get(f"https://digidates.de/api/v1/age/{birthdate}")

data = response.json()

print(data)
print(data["age"])
print(data["ageextended"]["years"],"years")
print(data["ageextended"]["months"],"months")
print(data["ageextended"]["days"],"days")