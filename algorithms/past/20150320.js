//http://www.careercup.com/question?id=5702361131515904

var arboreal = require('./libs/arboreal.js');
var util = require('util');

function main(tree, min, max){
	curr = tree.data;
	if (curr > max || curr < min)
	{
		return false;
	}
	if (tree.children.length == 0)
	{
		return true;
	}
	//unfortuantely for this data structure there is not concept of left or right child, so if 1 child only, I just assume it's ok
	if (tree.children.length == 2)
	{
		left = tree.children[0].data;
		right = tree.children[1].data;
		if (left <= curr && curr <= right)
		{
			//this is fine
		}
		else
		{
			return false;
		}
	}
	//so we know this level is ok, now we need to recursively call children
	return main(tree.children[0], min, curr) && main(tree.children[1], curr, max);
}


        //  5
        // 1 8
var tree1 = new arboreal.Arboreal();
tree1.appendChild(5); //root
tree1.children[0].appendChild(1).appendChild(8);
console.log(main(tree1.children[0], -999, 999) == true);

       //    5
       //  3   8
       // 4 2 
var tree2 = new arboreal.Arboreal();
tree2.appendChild(5); //root
tree2.children[0].appendChild(3).appendChild(8);
tree2.children[0].children[0].appendChild(4).appendChild(2);
console.log(main(tree2.children[0], -999, 999) == false);

       //    5
       //  3   8
       // 2 6 
var tree3 = new arboreal.Arboreal();
tree3.appendChild(5); //root
tree3.children[0].appendChild(3).appendChild(8);
tree3.children[0].children[0].appendChild(2).appendChild(6);
console.log(main(tree3.children[0], -999, 999) == false);
