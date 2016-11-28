def divide(num, den)
	display(num.to_f / den.to_f)
end

def display(result)
	puts sprintf("%.2f", result)
end

puts "What is the first operand?"
op_a = gets.chomp.to_f

puts "What is the second operand?"
op_b = gets.chomp.to_f

divide(op_a, op_b)