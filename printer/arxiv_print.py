from printer import Printer
import urllib
import lxml.html
import time

subs = ['cs.LG', 'stat.ML']

printer = Printer()
directory = "output.pdf"

def getUrls():
	list_of_urls = []
	for sub in subs:
		full_url = "http://arxiv.org/list/" + sub + "/pastweek?skip=0&show=5"
		connection = urllib.urlopen(full_url)
		dom =  lxml.html.fromstring(connection.read())
		for link in dom.xpath('//a/@href'):
			if "/pdf" in link:
				list_of_urls += ["http://arxiv.org" + link]
	return list(set(list_of_urls))

def arxiv_job():
	print "=== started arxiv job ==="
	urls = getUrls()
	for url in urls:
		printer.printUrl(url, directory, 1, 2)
		time.sleep(5)
	print "=== finished reddit job ==="

arxiv_job()
