import pytest
import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class TestTest:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_test(self):
        accounts = []
        with open("./accounts.csv", mode="r") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                accounts.append(
                    {"username": row["username"], "password": row["password"]}
                )
        i = 0
        for account in accounts:
            self.driver.get("https://www.saucedemo.com/")
            self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").click()
            self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys(account["username"])
            self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").click()
            self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys(account["password"])
            self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
            try:
                WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".shopping_cart_container")))
                print(f"Login successful for account {i} ({account['username']})")
                time.sleep(2)  # Wait for 2 seconds before proceeding
            except TimeoutException:
                print(f"Login failed for account {i} ({account['username']})")
            i += 1

if __name__ == "__main__":
    test = TestTest()
    test.setup_method(None)
    test.test_test()
    test.teardown_method(None)
