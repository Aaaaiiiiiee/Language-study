input_password = input("Please input your password: ")
print(type(input_password))

real_egoing_password = "11"
real_k8805_password = "ab"

if real_egoing_password == input_password:
    print("Hello!, egoing")
elif real_k8805_password == input_password:
    print("Hello!, k8805")
else:
    print("Who are you")