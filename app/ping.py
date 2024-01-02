import os
import logging
import datetime

logging.basicConfig(
    filename="artifact/ping_result.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


class PingTest:
    def __init__(self):
        self.hostname = "google.com"

    def run_test(self):
        # Ping Hostname
        response = os.system("ping -c 1 " + self.hostname)
        if response == 0:
            print(f"{self.hostname} is up!")
        else:
            print(f"{self.hostname} is down!")

    def close(self):
        pass


if __name__ == "__main__":
    # Example usage:
    speed_test_instance = PingTest()
    speed_test_instance.run_test()
    speed_test_instance.close()
