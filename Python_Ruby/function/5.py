def login(_id):
    members = ['egoing', 'k8805', 'leezche']
    
    for member in members:
        if member == _id:
            return True
    
    return False

input_id = input("Please input your id\n")

if(login(input_id)):
    print('Hello, ' + input_id)
else:
    print('Who are you?')