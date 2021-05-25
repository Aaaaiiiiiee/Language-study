input_password = input("Please input your password: ")

real_egoing_password = "egoing"
real_k8805_password = "k8805"

if real_egoing_password == input_password or real_k8805_password == input_password:
    print("Hello!")
else:
    print("Who are you")