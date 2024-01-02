import schedule
import time
import pushrank

def job_pushrank():
    speed_test_instance = pushrank.SpeedTest()
    speed_test_instance.run_test()
    speed_test_instance.close()

# schedule.every(10).seconds.do(job)
schedule.every(30).minutes.do(job_pushrank)
# schedule.every().day.at("10:30").do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)