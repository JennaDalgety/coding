puts "what is your first name?"
first_name = gets.chomp
puts "what is your last name?"
last_name = gets.chomp
puts "Welcome to the analyzer, #{first_name} #{last_name}."
puts "Your first name is #{first_name.length} characters long."
puts "Your last name is #{last_name.length} characters long."
puts "Your name is #{first_name.reverse} #{last_name.reverse} backwards."