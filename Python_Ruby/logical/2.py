input_id = input("Please input your id: ")
input_password = input("Please input your password: ")

real_id = "egoing"
real_password = "11"

if real_id == input_id:
    if real_password == input_password:
        print("Hello!")
    else:
        print("wrong password")
else:
    print("wrong id")