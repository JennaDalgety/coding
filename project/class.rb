class Dog

	def speak
		puts "Woof!"
	end

	def chew_on_bone
		puts"Mmmm..."
	end

	def chase_a_cat
		kitten = Cat.new
		puts "Bark!  Bark!"
		kitten.run_away
	end

end