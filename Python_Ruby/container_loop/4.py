input_password = input("Please input your password: ")

# real_egoing_password = "egoing"
# real_k8805_password = "k8805"
members = ['egoing', 'k8805']

# for member in members:
#     if member != input_password:
#         if member == members[len(members) - 1]:
#             print("Who are you")
#         continue
#     else:
#         print("Hello!, " + member)
#         break

for member in members:
    if member == input_password:
        print('Hello!, ' + member)
        import sys
        sys.exit()
print('Who are you?')