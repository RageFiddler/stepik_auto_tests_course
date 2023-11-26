from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)
price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"$100"))
book = browser.find_element(By.ID, "book").click()
x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)
answer_field = browser.find_element(By.ID, "answer").send_keys(y)
button = browser.find_element(By.ID, "solve").click()
time.sleep(12)
browser.quit()
