var schema = require('./schema.js');

function updatePriority(person) {
	var oneDay = 24*60*60*1000; // hours*minutes*seconds*milliseconds
	var daysSinceLastContact = Math.round(Math.abs(
		((new Date()).getTime() - person.lastContacted.getTime())/(oneDay)
	));
	var daysOverdue = daysSinceLastContact - person.cycle;
	if (daysOverdue <= 0)
	{
		person._score = 0;
	}
	else
	{
		person._score = daysOverdue * person.weight;
	}
	person.save();
}

function updatePriorities(){
	schema.Person.find({}, function(err, users) {
		for (var i=0; i < users.length; i++){
            var p = users[i];
			updatePriority(p);
		}
    });
}

module.exports = {
  updatePriority: updatePriority,
  updatePriorities: updatePriorities
};