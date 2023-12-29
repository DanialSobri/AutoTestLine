from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time

class SpeedTest:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def run_test(self):
        self.driver.get("https://unifi-my.speedtestcustom.com/?serverId=19302")
        print("Finding")
        
        btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#main-content > div.button__wrapper > div > button')))
        print("Button GO:", btn.is_displayed())
        btn.click()

        again_btn = WebDriverWait(self.driver, 300).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#root > div > span > div.test.test--finished.test--in-progress > div.container > main > div > button')))
        print("Result is out:", again_btn.is_displayed())

        time_result = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        ping_result_ms = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#root > div > span > div.test.test--finished.test--in-progress > div.container > main > section.results-container.results-container-stage-finished > div.results-latency > div.result-tile.result-tile-ping > div.result-body > div > div > span'))).text
        jitter_result_ms = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#root > div > span > div.test.test--finished.test--in-progress > div.container > main > section.results-container.results-container-stage-finished > div.results-latency > div.result-tile.result-tile-jitter > div.result-body > div > div > span'))).text
        download_result_mbps = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#root > div > span > div.test.test--finished.test--in-progress > div.container > main > section.results-container.results-container-stage-finished > div.results-speed > div.result-tile.result-tile-download > div.result-body > div.result-value > div > span'))).text
        upload_result_mbps = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#root > div > span > div.test.test--finished.test--in-progress > div.container > main > section.results-container.results-container-stage-finished > div.results-speed > div.result-tile.result-tile-upload > div.result-body > div.result-value > div > span'))).text

        result = {
            'timestamp': time_result,
            'ping': ping_result_ms,
            'jitter': jitter_result_ms,
            'download': download_result_mbps,
            'upload': upload_result_mbps
        }

        self.driver.save_screenshot("C:/Users/TM39967/Workspaces/AutoTestLine/artifact/testline.png")
        time.sleep(2)
        print("Testline result:", result)

    def close(self):
        self.driver.close()

# Example usage:
speed_test_instance = SpeedTest()
speed_test_instance.run_test()
speed_test_instance.close()
