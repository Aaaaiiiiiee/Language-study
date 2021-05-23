puts("Please input your password")
input_password = gets.chomp()

real_egoing_password = "11"
real_k8805_password = "ab"

if real_egoing_password == input_password
    puts("Hello!, egoing")
elsif real_k8805_password == input_password
        puts("Hello!, k8805")
else
    puts("Who are you")
end