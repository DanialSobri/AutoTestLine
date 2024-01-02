import schedule
import time
import pushrank

def job_pushrank():
    try:
        speed_test_instance = pushrank.SpeedTest()
        speed_test_instance.run_test()
        speed_test_instance.close()
    except:
        speed_test_instance = pushrank.SpeedTest()
        speed_test_instance.run_test()
        speed_test_instance.close()

# schedule.every(60).seconds.do(job_pushrank)
schedule.every(20).minutes.do(job_pushrank)
# schedule.every().day.at("10:30").do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)