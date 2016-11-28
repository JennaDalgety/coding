$words = %w(the quick brown fox jumped over the lazy dog)

def frequency(word)
	arr = $words.select do |sample|
		word == sample
	end
	arr.size
end

frequencies = $words.uniq.map do |word|
	[word, frequency(word) ]
end

sorted = frequencies.sort do |a, b|
	b[-1] <=> a[-1]
end
p sorted