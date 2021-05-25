puts("Please input your password")
input_password = gets.chomp()

real_egoing_password = "egoing"
real_k8805_password = "k8805"

if real_egoing_password == input_password or real_k8805_password == input_password
    puts("Hello!")
else
    puts("Who are you")
end