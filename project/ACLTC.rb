puts "Welcome to my exercise!  Please enter five words:"

words = []

5.times do
	puts "Enter a word:"
	words << gets.chomp
end

new_array = words.sort

puts
puts "Here is your list of words:"

counter = 0
new_array.each do |word|
	if counter % 2 == 0
		puts word.upcase
	else 
		puts word
	end
	counter += 1
end
