import random
import string

print("Welcome to Random Password Generator!")

randchar="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_@"
nmofpwd=int(input("Please enter the No.of Passwords to be Generated:"))
pwdlen=int(input("Please enter the length of the Password needed:"))

print("Here is your Random Passwords:")

for x in range(nmofpwd):
    pwd=''.join(random.choice(randchar))
    for chars in range(pwdlen):
        pwd= pwd + random.choice(randchar)

        print(pwd)








