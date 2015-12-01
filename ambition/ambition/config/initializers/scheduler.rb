require 'rufus-scheduler'
require 'gmail'
require 'date'

$ip = "127.0.0.1:3000/"
$gmail_user = ""
$gmail_pass = ""
$user_email = ""

def email_auto(topic, content)
	gmail = Gmail.new($gmail_user, $gmail_pass)
		email = gmail.generate_message do
  			to $user_email
  			subject topic
  			body content
		end
		gmail.deliver(email)
	gmail.logout
end

# on sunday morning, email new week's goal sheet
def tentative_create_weekly_goals
	upcoming_monday = DateTime.now + 1
	url = $ip + "goalsheets/new"
	content = "Hey,\n\nIt's a new week. Plan how you wanna dominate the world. " + url
	email_auto("create weekly goal", content)
end

#on sunday morning, email last week's goal sheet
def tentative_conclude_weekly_goals
	past_monday = DateTime.now - 5
	@goalsheet = Goalsheet.where(:time => (past_monday - 2).to_time..(past_monday + 1).to_time)
	url = $ip + "goalsheet/" + @goalsheet[0].id.to_s
	content = "Yo,\n\nFill out the results of your goalsheet: " + url
	email_auto("conclude weekly goal", content)
end

puts DateTime.now
scheduler = Rufus::Scheduler.new
scheduler.cron '00 05 * * 0' do
	tentative_conclude_weekly_goals
	tentative_create_weekly_goals
end