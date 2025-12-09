import bcrypt

password = b"qwerty123"
hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
print(hashed_password)

input_password = bytes(input("enter your password"), encoding='utf-8')

if bcrypt.checkpw(input_password, hashed_password):
    print("Login successful")

else:
    print("You entered an invalid password")
