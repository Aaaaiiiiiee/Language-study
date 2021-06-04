array = [1, 3, 56, 7, 13, 52]
puts 'BEFORE ', array, "\n"

array.delete_if() do |item|
    item > 7
end

# use {}, if your code is only one line.
# use `do ~ end`, if your codes are multi lines.

puts 'AFTER ', array