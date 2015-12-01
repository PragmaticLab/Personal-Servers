var mongoose = require('mongoose');
mongoose.connect('mongodb://localhost/tap');

var db = mongoose.connection;
db.on('error', console.error.bind(console, 'connection error:'));
db.once('open', function (callback) {
  // yay!
});

var personSchema = mongoose.Schema({
	name: String,
	weight: Number, //how important
	src: String, //where you known this person
	contact: String, //how to contact the person
	cycle: Number, //contact in how many days?
	lastContacted: Date,
	_score: Number, //current internal score <-- how important is it for u to contact this person now
})

var Person = mongoose.model('Person', personSchema);

module.exports = {
  Person: Person,
};
