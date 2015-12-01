var schema = require('./schema.js');
var fs = require('fs');

var data = [];

schema.Person.find({}, function(err, users) {
	for (var i=0; i < users.length; i++){
        var p = users[i];
		data.push({name: p.name, weight: p.weight, src: p.src, contact: p.contact, cycle: p.cycle, lastContacted: p.lastContacted});
	}
	var dataJSON = JSON.stringify(data);

	fs.writeFile("dump.txt", dataJSON, function(err) {
    	if(err) {
        	console.log(err);
    	} else {
        	console.log("The file was saved!");
    	}
	}); 
});
