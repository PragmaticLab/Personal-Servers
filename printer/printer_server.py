import schedule
import time
from reddit_print import reddit_job

schedule.every().day.at("20:41").do(reddit_job)

while True:
    schedule.run_pending()
    time.sleep(1)
