#http://www.careercup.com/question?id=5696664260050944
#basically BFS

def getNextSquares(field, coord):
	next_list = []
	x,y = coord
	#top square
	if y - 1 >= 0 and field[y-1][x] == 0:
		next_list += [(x, y-1)]
	if x - 1 >= 0 and field[y][x-1] == 0:
		next_list += [(x-1, y)]
	if y + 1 < len(field) and field[y+1][x] == 0:
		next_list += [(x, y+1)]
	if x + 1 < len(field[0]) and field[y][x+1] == 0:
		next_list += [(x+1, y)]
	return next_list

def main(field, p, q):
	queue = []
	queue += [[p]]
	while queue:
		path = queue.pop(0)
		last_node = path[-1]
		if last_node == q:
			return path
		next_list = getNextSquares(field,last_node)
		for node in next_list:
			if node not in path:
				new_path = list(path)
				new_path.append(node)
				queue.append(new_path)

# main()
map1 =\
[[0, 0, 0],\
[1, 1, 0],\
[0, 0, 0]]
p1 = (0, 0)
q1 = (2, 2)

print main(map1, p1, q1) #1 step at a time

map2 =\
[[0, 1, 0],\
[1, 1, 0],\
[0, 0, 0]]
p2 = (0, 0)
q2 = (1, 1)
print main(map2, p2, q2) # none, cuz impossible
