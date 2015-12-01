//http://www.careercup.com/question?id=5106830093058048
package main
import "fmt"

type employee struct {
    id int
    manager_id  int
}

//returns # of employees that directly work for {id}
func direct(id int, list *[]employee) int {
	num := 0
	for _, employee := range *list {
        if employee.manager_id == id{
        	num += 1
        }
    }
	return num;
}

//todo: the indirect fn
//construct a tree that stores how many children it has

func main() {
	company_list := []employee{employee{1, 0}, employee{2, 1}, employee{3, 1}, employee{4, 2}}

	fmt.Println(direct(1, &company_list))
}

