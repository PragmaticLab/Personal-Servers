//http://www.careercup.com/question?id=5673481771417600
package main
import "fmt"

//returns the water lvl inside a dip
func water(start int, end int, bars []int) int {
	var highest int = bars[start]
	if bars[start] > bars[end]{
		highest = bars[end]
	}

	sum := 0
	for i:= start + 1; i < end; i++{
		sum = sum + (highest - bars[i])
	}
	return sum
}

//creates a bunch of segments and then add water to each segment
func separate(bars []int) int {
	first:= true
	amount:= 0
	start:= -1
	prev:= -1
	curr:= -1
	for i:= 0; i < len(bars); i++{
		curr = bars[i]
		// fmt.Println(curr);
		if prev == -1{
			start = i
			prev = curr
			// fmt.Println("A");
		} else if (prev > curr || i == len(bars) - 1) && !first{
			// fmt.Println("C");
			if i == len(bars) - 1{
				amount += water(start, i, bars)
			} else{
				amount += water(start, i - 1, bars)
			}
			start = i - 1
		} else {
			first = false
			// fmt.Println("B");
			//nothing i guess
		} 
		prev = curr
		// fmt.Println("\n");
	}
	return amount
}

func main() {
	bars1 := []int{5, 1, 1, 1, 5}

	fmt.Println(separate(bars1));
}

