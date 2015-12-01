var schema = require('./schema.js');
var nodemailer = require('nodemailer');
var fs = require('fs');
var settings = JSON.parse(fs.readFileSync('./config.json', 'utf8'));

var MAX_CONTACTS_PER_DAY = 3;


var transporter = nodemailer.createTransport({
    service: 'Gmail',
    auth: {
        user: settings['gmail_user'],
        pass: settings['gmail_pass']
    }
});

var DEFAULT_HTML = '<p>Here are the people to contact:</p><br><br>';

var mailOptions = {
    from: settings['gmail_user'], 
    to: settings['email'],
    subject: 'tap - get in touch with these people',
    html: DEFAULT_HTML
};

function mailPriority(){
    var num = 0;
    mailOptions['html'] = DEFAULT_HTML;
    schema.Person.find({}, null, {sort: {'_score': -1}},function(err, users) {
        for (var i=0; i < users.length; i++){
            var p = users[i];
            if (p._score <=0 )
            {
                break;
            }
            if (num == MAX_CONTACTS_PER_DAY )
            {
                break;
            }
            num += 1;
            var profile_url = settings['server_address'] + 'person/' + p._id.toString();
            var contact_url = settings['server_address'] + 'contact/' + p._id.toString();
            mailOptions['html'] += '<a href="' + profile_url + '">' + p.name + '</a>'
            mailOptions['html'] += ' <a href="' + contact_url + '">contacted!</a>' + '<br>'
        }
        if (num > 0) //dont need to email if no one to contact
        {
            transporter.sendMail(mailOptions, function(error, info){
                if(error){
                    console.log(error);
                }else{
                    console.log('Message sent: ' + info.response);
                }
            });
        }
    });
}

module.exports = {
  mailPriority: mailPriority,
};