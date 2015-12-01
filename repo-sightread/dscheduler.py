import schedule
import time
import json
from github import getUrls
from email_local import mail

raw=open('config.json')
config = json.load(raw)
languages = config['languages']

def job():
	mail(getUrls(languages))
	print("emailed!")

schedule.every().day.at("11:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)