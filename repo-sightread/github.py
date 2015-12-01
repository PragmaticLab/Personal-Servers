from __future__ import division
import requests, json
import random
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth('yasmite', 'yasmite123')
MAX_REPO_ID = 31000000

auths = []
auths.append(HTTPBasicAuth('godzillabitch', 'godzillabitch123'))
auths.append(HTTPBasicAuth('ankitsmarty', 'ankitsmarty123'))
auths.append(HTTPBasicAuth('yasmite', 'yasmite123'))
auths.append(HTTPBasicAuth('qwertybitch', 'qwertybitch123'))
auths.append(HTTPBasicAuth('andrewnoobee', 'andrewnoobee123'))
auths.append(HTTPBasicAuth('threelegged', 'threelegged123'))
auths.append(HTTPBasicAuth('ninewindows', 'ninewindows123'))
auths.append(HTTPBasicAuth('twittch', 'twittch123'))
auths.append(HTTPBasicAuth('phenoixtt', 'phenoixtt123'))
auths.append(HTTPBasicAuth('bootcampee', 'bootcampee123'))
auths.append(HTTPBasicAuth('lolmoob', 'lolmoob123'))
auths.append(HTTPBasicAuth('biggyt', 'biggyt123'))
auths.append(HTTPBasicAuth('tomatodude', 'tomatodude123'))
auths.append(HTTPBasicAuth('potatodude', 'potatodude123'))
auths.append(HTTPBasicAuth('friedricedude', 'friedricedude123'))
auths.append(HTTPBasicAuth('chowmeindude', 'chowmeindude123'))
auths.append(HTTPBasicAuth('goodolddude', 'goodolddude123'))
auths.append(HTTPBasicAuth('cryingdude', 'cryingdude123'))
auths.append(HTTPBasicAuth('sennheiserdude', 'sennheiserdude123'))
auths.append(HTTPBasicAuth('beatsdude', 'beatsdude123'))
auths.append(HTTPBasicAuth('bosedude', 'bosedude123'))
auths.append(HTTPBasicAuth('sonydude', 'sonydude123'))
auths.append(HTTPBasicAuth('bobdylann', 'bobdylann123'))
auths.append(HTTPBasicAuth('godizllll', 'godizllll123'))
auths.append(HTTPBasicAuth('jliiii', 'jliiii123'))
auths.append(HTTPBasicAuth('sssssst', 'sssssst123'))
auths.append(HTTPBasicAuth('wwwtt', 'wwwtt123'))
auths.append(HTTPBasicAuth('uoftttt', 'uoftttt123'))
auths.append(HTTPBasicAuth('vanyee', 'vanyee123'))
auths.append(HTTPBasicAuth('yammmettt', 'yammmettt123'))


# determines if a repo has the required programming languages
# and if the programming language is used enough
def languageCheck(language_url, language):
	language = language.encode('UTF-8')
	r = requests.get(language_url, auth=random.choice(auths))
	languages = r.json()
	if language not in languages.keys():
		return False

	amount_from_language, total = languages[language], 0
	for name, val in languages.iteritems():
		total += val
	
	if total < 500 or amount_from_language < 300: #not enough lines
		return False
	if amount_from_language / total <= 0.1:
		return False
	return True


# returns a repo that matches description, none otherwise
def getRepo(id, language="CSS"):
	try:
		r = requests.get("https://api.github.com/repositories?since=" + str(id), auth= random.choice(auths))
	except:
		return None
	repos = r.json()

	if len(repos) <= 3: #something wrong with api, just redo
		return None 

	# now that we got a random repo, we need to try to match language
	for repo in repos:
		repo_langauge_url = repo['url'] + "/languages"
		if languageCheck(repo_langauge_url, language):
			return repo['html_url']
	return None

def getUrls(languages=['Python', 'Ruby']):
	repoID = random.random() * MAX_REPO_ID
	urls = []

	for language in languages:
		repo = None
		while not repo:
			# print "attempt!"
			repoID = random.random() * MAX_REPO_ID
			repo = getRepo(repoID, language)
		urls += [repo]

	return urls
