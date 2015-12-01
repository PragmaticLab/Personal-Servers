#http://www.careercup.com/question?id=5186461135536128



def main(array, n=1)
	hash = {}
	for i in 0..array.length-1
		num = array[i]
		if hash.has_key?(num)
			hash[num] += 1
		else
			hash[num] = 0
		end
	end
    return hash.sort_by {|_key, value| _key}.reverse[0..n]
end

puts main([0, 0, 100, 3, 5, 4, 6, 4, 2, 100, 2, 100], 2)
