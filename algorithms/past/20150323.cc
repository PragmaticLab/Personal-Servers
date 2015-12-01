//http://www.careercup.com/question?id=5694220289441792
#include <iostream>
#include <string>
#include <vector>

class ReverseNode {
 	public:
 		int val;
 		ReverseNode * parent;
 		//root constructor
 		ReverseNode(int val){
 			this->val = val;
 			this->parent = NULL;
 		}
 		//normal constructor
 		ReverseNode(int val, ReverseNode *node){
 			this->val = val;
 			this->parent = node;
 		}
};

//finds 1st common ancestor
ReverseNode* findAncestor(ReverseNode * n1, ReverseNode * n2){
	ReverseNode * other = n2;
	while (n1 != NULL){
		while(n2 != NULL){
			if (n1 == n2){
				return n1;
			}
			n2 = n2->parent;
		}
		n2 = other; //reset what n2 is 
		n1 = n1->parent;
	}

	return NULL;
}


int main(int argc, char* argv[])
{
	//       0
	//    1     2
	//  3
	// 4
	ReverseNode root(0);
	ReverseNode c1(1, &root);
	ReverseNode c2(2, &root);
	ReverseNode c3(3, &c1);
	ReverseNode c4(4, &c3);

	std::cout << (*findAncestor(&c3, &c4)).val;
	std::cout << (*findAncestor(&c3, &c2)).val;
	std::cout << (*findAncestor(&c4, &c1)).val;

    return 0;
}

