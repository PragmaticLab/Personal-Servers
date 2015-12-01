//http://programmers.stackexchange.com/questions/275676/interview-question-robot-in-a-grid

function robo(m, n){
	return step_helper(1, 1, m, n);
}

function step_helper(i, j, m, n){
	// console.log(i, j, m, n);
	if (i == m && j == n){
		return 0;
	}
	if (i > m || j > n){
		return 9999;
	}
	var down_steps = 1 + step_helper(i+j, j, m, n);
	var right_steps = 1 + step_helper(i, i+j, m, n);
	var smallest = (down_steps < right_steps ? down_steps : right_steps);
	// console.log(down_steps, right_steps, smallest);
	return smallest;
}

console.log(robo(1,1), robo(1,1) == 0);
console.log(robo(3,2), robo(3,2) == 2);
console.log(robo(3,5), robo(3,5) == 3);

