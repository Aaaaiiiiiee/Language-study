require_relative 'auth'

puts("Please input your password")
input_id = gets.chomp()

if(Auth.login(input_id))
    puts('Hello, ' + input_id)
else
    puts('Who are you?')
end