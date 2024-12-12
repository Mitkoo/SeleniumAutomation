import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def test_driver():
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.bnb.bg")

    rate = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/ul/li[1]/strong')
    print(rate.text)
    time.sleep(5)


if __name__ == '__main__':
    test_driver()
