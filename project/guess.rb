puts "Welcome to the number guessing game."
puts "Guess a number between 1 and 100"
answer = rand(100)

10.times do
	guess = gets.chomp.to_i

	if guess == answer
		puts "You win!"
		exit
	else
		puts "Nope.  Guess another number."
	end
end

puts "You lose!"