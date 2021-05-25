puts("Please input your id")
input_id = gets.chomp()
puts("Please input your password")
input_password = gets.chomp()

real_id = "egoing"
real_password = "11"

if real_id == input_id and real_password == input_password
        puts("Hello!")
else
    puts("You've got wrong information")
end