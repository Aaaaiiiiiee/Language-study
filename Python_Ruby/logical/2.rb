puts("Please input your id")
input_id = gets.chomp()
puts("Please input your password")
input_password = gets.chomp()

real_id = "egoing"
real_password = "11"

if real_id == input_id
    if real_password == input_password
        puts("Hello!")
    else
        puts("wrong password")
    end
else
    puts("wrong id")
end