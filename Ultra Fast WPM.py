from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.keyhero.com/free-typing-test/")

driver.find_element_by_class_name("cookiebanner").send_keys(Keys.ESCAPE)

text_box = driver.find_element_by_class_name("user-input-text")
time.sleep(1)
first_word = driver.find_elements_by_xpath('.//span[@class = "quote-current"]')[0]

text_box.send_keys(str(first_word.text))

quote_right = driver.find_elements_by_xpath('.//span[@class = "quote-right"]')[0]
text_box.send_keys(Keys.SPACE)
time.sleep(1)
text_box.send_keys(str(quote_right.text))

while True:
    time.sleep(0.5)
    fix_error = driver.find_elements_by_xpath('.//span[@class = "quote-error"]')[0]
    text_box.send_keys(str(fix_error.text))
    for _ in range(len(fix_error.text)):
        text_box.send_keys(Keys.BACKSPACE)
    quote_right = driver.find_elements_by_xpath('.//span[@class = "quote-right"]')[0]
    text_box.send_keys(Keys.SPACE)
