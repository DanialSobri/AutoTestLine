from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import time

class Streaming:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def run_test(self):
        print("Start Streaming Testline ...")
        self.driver.get("https://www.youtube.com/watch?v=LXb3EKWsInQ")
        
        # Play video
        btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > button')))
        btn.click()

        print("Setup Environment ...")

        # Select 4K
        self.driver.find_element(By.CSS_SELECTOR, value='button.ytp-button.ytp-settings-button').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, value="/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[30]/div/div/div[4]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, value='(//div[@class="ytp-menuitem"])[1]').click()

        # Open stats for nerds
        time.sleep(5)
        actionChains = ActionChains(self.driver)
        video_area = WebDriverWait(self.driver, 300).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#movie_player > div.html5-video-container > video')))
        actionChains.context_click(video_area).send_keys(Keys.ARROW_DOWN).perform()
        pyautogui.press('down')
        time.sleep(1)
        pyautogui.press('down')
        time.sleep(1)
        pyautogui.press('down')
        time.sleep(1)
        pyautogui.press('down')
        time.sleep(1)
        pyautogui.press('down')
        time.sleep(1)
        pyautogui.press('down')
        time.sleep(1)
        pyautogui.press('down')
        time.sleep(1)
        pyautogui.press('space')

        print("Testing ...")
        
        # Wait until the middle of video 
        time.sleep(150)

        # Screen capture
        self.driver.save_screenshot("C:/Users/TM39967/Workspaces/AutoTestLine/artifact/testline_streaming.png")
        print("Streaming Testline Finished")

    def close(self):
        self.driver.close()

if __name__ == "__main__":
    # Example usage:
    speed_test_instance = Streaming()
    speed_test_instance.run_test()
    speed_test_instance.close()
