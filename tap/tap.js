var express = require('express');
var app = express();
app.set('views', __dirname + '/views');
app.use(express.static(__dirname + '/public'));
var schema = require('./schema.js');
var priority = require('./priority.js');
var bodyParser = require('body-parser');
app.use(bodyParser.urlencoded());
var ObjectId = require('mongoose').Types.ObjectId;

app.get('/', function (req, res) {
	res.render('index.jade', {title: 'Tap'});
})

app.get('/insert', function (req, res) {
	res.render('insert.jade', {});
})

app.post('/insert', function (req, res) {
	var name = req.body.name;
	var weight = req.body.weight;
	var src = req.body.src;
	var contact = req.body.contact;
	var cycle = req.body.cycle;
	var lastContacted = req.body.lastContacted;
	var newPerson = new schema.Person({name:name, weight:weight, src:src, contact:contact, cycle:cycle, lastContacted:lastContacted, _score:0});
	newPerson.save(function (err) {if (err) console.log ('Error on save!')});
	priority.updatePriority(newPerson);
	res.redirect('/');
})

app.get('/all', function (req, res){
	schema.Person.find({}, function(err, users) {
    	res.render('all.jade', {people: users});
    });
})

//this should prob be a POST
app.get('/contact/:objid', function (req, res){
	var objid = req.param("objid");
	schema.Person.findOne({_id: new ObjectId(objid)}, function(err,obj) {
		obj.lastContacted = new Date();
		obj.save();
		priority.updatePriority(obj);
	});
	var all = schema.Person.find({}, function(err, users) {
		res.redirect('/all');
    });
})

//this should prob also be a psot
app.get('/delete/:objid', function (req, res){
	var objid = req.param("objid");
	schema.Person.findByIdAndRemove({_id: new ObjectId(objid)}, function(err, docs){
		if(err) res.json(err);
		else    res.redirect('/all');
	});
})

app.get('/person/:objid', function (req, res){
	var objid = req.param("objid");
	schema.Person.findOne({_id: new ObjectId(objid)}, function(err,obj) {
		res.render('person.jade', {person: obj});
	});
})

app.post('/person/:objid', function (req, res){
	var name = req.body.name;
	var weight = req.body.weight;
	var src = req.body.src;
	var contact = req.body.contact;
	var cycle = req.body.cycle;
	var lastContacted = req.body.lastContacted;

	var objid = req.param("objid");
	schema.Person.findOne({_id: new ObjectId(objid)}, function(err,obj) {
		obj.name = name;
		obj.weight = weight;
		obj.src = src;
		obj.contact = contact;
		obj.cycle = cycle;
		obj.lastContacted = lastContacted;
		obj.save();
		priority.updatePriority(obj);
	});
	res.redirect('/all');
})

app.get('/score', function (req, res){
	var all = schema.Person.find({}, null, {sort: {'_score': -1}},function(err, users) {
    	res.render('score.jade', {people: users});
    });
})

app.get('/priority', function (req, res){
	var all = schema.Person.find({}, null, {sort: {'weight': -1}},function(err, users) {
    	res.render('priority.jade', {people: users});
    });
})

var server = app.listen(3000, function () {
	var host = server.address().address
	var port = server.address().port
	console.log('listening at http://%s:%s', host, port)
})