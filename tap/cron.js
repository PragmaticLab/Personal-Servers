var priority = require('./priority.js');
var mailer = require('./mailer.js');

function dailyRun(){
	console.log("started job for " + (new Date()).toString());
	priority.updatePriorities();
	mailer.mailPriority();
}

var CronJob = require('cron').CronJob;
new CronJob('* 30 11 * * *', function(){
    dailyRun();
}, null, true, "America/Los_Angeles");
