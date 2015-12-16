from printer import Printer
import praw
import time

SUBREDDITS = ['MachineLearning']
printer = Printer()
directory = "output.pdf"

def getUrls():
	list_of_urls = []
	r = praw.Reddit(user_agent='top500scraper by u/archon_rising')
	for subreddit in SUBREDDITS:
		sub = r.get_subreddit(subreddit)
		for post in sub.get_hot(limit=10):
			list_of_urls += [post.url]
	return list_of_urls

def reddit_job():
	print "=== started reddit job ==="
	urls = getUrls()
	for url in urls:
		if "." in url[-4:-1]: # if it's a pdf file
			printer.printUrl(url, directory, 1, 2)
		else:
			printer.printUrl(url, directory, 1, 2)
		time.sleep(10)
	print "=== finished reddit job ==="
