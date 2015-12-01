#!/usr/bin/python

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os
import json

raw=open('config.json')
config = json.load(raw)
gmail_user = config['gmail_user']
gmail_pwd = config['gmail_pass']

def mail(url_list, subject="Repo-SightRead Today", to=config['email'], attach=None):
	text = emailMsg(url_list)
	msg = MIMEMultipart()

	msg['From'] = gmail_user
	msg['To'] = to
	msg['Subject'] = subject

	msg.attach(MIMEText(text))

	mailServer = smtplib.SMTP("smtp.gmail.com", 587)
	mailServer.ehlo()
	mailServer.starttls()
	mailServer.ehlo()
	mailServer.login(gmail_user, gmail_pwd)
	mailServer.sendmail(gmail_user, to, msg.as_string())
	# Should be mailServer.quit(), but that crashes...
	mailServer.close()

def emailMsg(url_list):
	msg = "This is an email from repo-sightread.\n\n\n"
	msg += "repos to read today: \n"
	for url in url_list:
		msg += url
		msg += "\n"
	return msg
