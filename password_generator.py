import random
length_password=int(input("Enter your password length:"))
characters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
password=""
for i in range(length_password):
    random_choice=random.choice(characters)
    password=password+random_choice
print(password)
