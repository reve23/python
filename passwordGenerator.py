import random
import string

while True:
    try:
        password_len = int(input("Enter password length : "))
        real_password = string.ascii_letters + string.digits + string.punctuation
        password = []
        for x in range(password_len):
            password.append(random.choice(real_password))

        print(''' 

        ''')
        print("".join(password))

    except:
        print("Please enter password length in number")