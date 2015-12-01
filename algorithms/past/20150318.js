//http://www.careercup.com/question?id=5635749544198144

function shift(str){
	if (str.length % 2 == 0)
	{
		return str.split("").reverse().join("");
	}
	else
	{
		return str.toUpperCase();
	}
}


function main(str){
	segments = str.split(' ');
	new_segments = segments.slice();
	for (var i = 0; i < segments.length; i++){
		seg = segments[i];
		//must remove the punctuations
		seg_no_punc = seg.replace(/[^a-zA-Z0-9]/g,'');
		clean_seg = seg.slice(0,seg_no_punc.length);
		punc = seg.slice(seg_no_punc.length);
		new_segments[i] = shift(clean_seg) + punc;
	}
	return new_segments.join(" ");
}

var str1 = "this is a test";
var str2 = "even odd even odd odd";
var str3 = "this sentence has punctuation!!!!";
var str4 = "this sentence has punctuationn!!!!";

console.log(main(str1));
console.log(main(str2));
console.log(main(str3));
console.log(main(str4));
