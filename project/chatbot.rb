puts "Hi, my name is Ruby!"
puts "What is your name?"
name = gets.chomp
puts "Hi, #{name}!"
question = gets.chomp
if question == 'How old are you?'
	puts "20 years old."
end
if question == 'Where do you live?'
	puts "Japan."
end