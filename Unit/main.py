file = open('user.csv','a')
file = open('user.csv','r')
lines = file.readlines()
users = dict()
for line in lines:
    name = line.replace("\n","").split(",")[0]
    password = line.replace("\n","").split(",")[1]
    users[name]=password
file.close()


username = input("username:")
password = input("password")
if username not in users.key():
    file.write(f'{username},{password}\n')
else:
    print('the username has already taken by another user!')


