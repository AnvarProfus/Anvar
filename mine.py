import random
simvoli = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
dlina = int(input("Введи нужную длинну пароля"))
password = ""
for i in range(dlina):
    password += random.choice(simvoli)
print(password)