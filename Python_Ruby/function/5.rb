def login(id)
    members = ['egoing', 'k8805', 'leezche']
    for member in members do
        if member == id
            return true
        end
    end
    return false
end

puts("Please input your password")
input_id = gets.chomp()

if(login(input_id))
    puts('Hello, ' + input_id)
else
    puts('Who are you?')
end