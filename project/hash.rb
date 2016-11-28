
prizes = {"red" => "A new car!!!", "yellow" => "A million dollars!!!", "green" => "A hamster."}

puts "Congratulations! Choose the box that holds your prize: yellow, red or green."

choice = gets.chomp

puts "You've won..." + prizes[choice]