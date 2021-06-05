name = 'egoing'
name = String.new('egoing')
# It is same result that above two lines.

name1 = String.new('egoing')
name2 = String.new('k8805')

puts(name1.reverse())
puts(name2.reverse())
puts()

puts(name1.upcase())
puts(name1.size())
puts()

names = Array.new
names.push('egoing')
names.push('k8805')

puts(names)
puts names.join(',')
puts()