words = %w(the quick brown fox jumped over the lazy dog)
words.find.uniq do |word|
	puts word
end