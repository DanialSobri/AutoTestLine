from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time
import logging

logging.basicConfig(filename='artifact/pushrankokla.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SpeedTest:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def run_test(self):
        print("Start Push Rank")
        self.driver.get("https://www.speedtest.net/")
        self.driver.maximize_window()
        time.sleep(1)
        
        # Enable cookie
        btn_cookie = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#onetrust-accept-btn-handler')))
        print("Button Cookie:", btn_cookie.is_displayed())
        btn_cookie.click()

        time.sleep(1)

        btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#container > div > div.main-content > div > div > div > div.pure-u-custom-speedtest > div.speedtest-container.main-row > div.start-button')))
        print("Button GO:", btn.is_displayed())
        btn.click()

        again_btn = WebDriverWait(self.driver, 300).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#container > div > div.main-content > div > div > div > div.pure-u-custom-speedtest > div.speedtest-container.main-row > div.main-view > div > div.result-area.result-area-test > div > div > div.result-container-speed.result-container-speed-active > div.result-container-data > div.result-item-container.result-item-container-align-center > div > div.result-data.u-align-left')))
        print("Result is out:", again_btn.is_displayed())

        time_result = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        # ping_result_ms = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#root > div > span > div.test.test--finished.test--in-progress > div.container > main > section.results-container.results-container-stage-finished > div.results-latency > div.result-tile.result-tile-ping > div.result-body > div > div > span'))).text
        # jitter_result_ms = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#root > div > span > div.test.test--finished.test--in-progress > div.container > main > section.results-container.results-container-stage-finished > div.results-latency > div.result-tile.result-tile-jitter > div.result-body > div > div > span'))).text
        download_result_mbps = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#container > div > div.main-content > div > div > div > div.pure-u-custom-speedtest > div.speedtest-container.main-row > div.main-view > div > div.result-area.result-area-test > div > div > div.result-container-speed.result-container-speed-active > div.result-container-data > div.result-item-container.result-item-container-align-center > div > div.result-data.u-align-left > span'))).text
        upload_result_mbps = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#container > div > div.main-content > div > div > div > div.pure-u-custom-speedtest > div.speedtest-container.main-row > div.main-view > div > div.result-area.result-area-test > div > div > div.result-container-speed.result-container-speed-active > div.result-container-data > div.result-item-container.result-item-container-align-left > div > div.result-data.u-align-left > span'))).text
        connection = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#container > div > div.main-content > div > div > div > div.pure-u-custom-speedtest > div.speedtest-container.main-row > div.main-view > div > div.result-area.result-area-test > div > div > div.result-container-speed.result-container-speed-active > div:nth-child(4) > div > div > div.pure-u-1-2.u-c.eot-info-test > div.result-item.result-item-align-left.result-item-icon.result-item-connection-mode > div.result-data'))).text
        server = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#container > div > div.main-content > div > div > div > div.pure-u-custom-speedtest > div.speedtest-container.main-row > div.main-view > div > div.result-area.result-area-test > div > div > div.result-container-speed.result-container-speed-active > div:nth-child(4) > div > div > div.pure-u-1-2.u-c.eot-info-test > div:nth-child(2) > div.result-label > a'))).text
        location = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#container > div > div.main-content > div > div > div > div.pure-u-custom-speedtest > div.speedtest-container.main-row > div.main-view > div > div.result-area.result-area-test > div > div > div.result-container-speed.result-container-speed-active > div:nth-child(4) > div > div > div.pure-u-1-2.u-c.eot-info-test > div:nth-child(2) > div.result-data.js-sponsor-name'))).text
        
        result = {
            'timestamp': time_result,
            # 'ping': ping_result_ms,
            # 'jitter': jitter_result_ms,
            'download': download_result_mbps,
            'upload': upload_result_mbps,
            'connection' : connection,
            'server' : server,
            'location' : location
        }

        # self.driver.save_screenshot("C:/Users/TM39967/Workspaces/AutoTestLine/artifact/testline.png")
        time.sleep(3)
        print("Testline result:", result)
        logging.info(result)

    def close(self):
        self.driver.close()

if __name__ == "__main__":
    # Example usage:
    speed_test_instance = SpeedTest()
    speed_test_instance.run_test()
    speed_test_instance.close()
