#http://www.careercup.com/question?id=5742921007497216
#so after we erase n nunbers, we always end up with a number made up of the same # of chars
#the smallest number possible needs the smallest character possible at the left most position
#so we always pick smallest and iterate

def helper(string, n)
	if string.length == n - 1
		return "", n - 1
	end
	smallest = 9999
	count = 0
	for i in 0..string.length-1
		char = string[i].to_i
		if char < smallest
			smallest = char
		end 
		count += 1
		if count == n
			# if i != string.length - 1 && string[i].to_i > string[i+1].to_i
			# 	smallest = string[i + 1].to_i
			# end
			break
		end
	end
	# now we know the smallest so we need to know where to break
	index = string.index(smallest.to_s)
	string = string[index..string.length]
	# puts string, index
	return string, index
end

def main(string, n)
	if string.length <= n
		return ""
	end
	if n == 0
		return string
	end

	return_string = ""

	# test = 1
	while n != 0
		string, minus = helper(string, n + 1)
		n = n - minus 
		if n == 0 && string != ""
			return return_string + string
		end
		if n == 0 && string == ""
			return return_string
		end
		if string == 0 && n != 0
			assert(false, "made an error somewhere before")
			return
		end

		if string != ""
			return_string += string[0]
			string = string[1..string.length]
		end
		# puts return_string, string, n
		# puts "-----------"
		# test += 1
		# if test == 6
		# 	break
		# end
	end
	return return_string
end

puts main("4205123", 4) #answer is 012
puts main("216504", 3) #104
