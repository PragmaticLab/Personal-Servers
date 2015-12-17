import schedule
import time
from reddit_print import reddit_job
from arxiv_print import arxiv_job

schedule.every().day.at("7:05").do(reddit_job)
schedule.every().day.at("7:15").do(arxiv_job)

while True:
    schedule.run_pending()
    time.sleep(1)
