class User
	attr_accessor :name, :age

	def initialize(name, age)
		self.name = name
		self.age = age
	end

	def print
		puts "Happy #{self.age + 1}st birthday, #{self.name}"
	end
end

user = User.new('Jenna', 36)
user.print