import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service


def login(username="//input[@id='username']", password="//input[@id='password']", button="//button[@type='submit']"):
    chrome.get("https://the-internet.herokuapp.com/login")
    chrome.find_element(By.XPATH, username).send_keys("tomsmith")
    time.sleep(2)
    chrome.find_element(By.XPATH, password).send_keys("SuperSecretPassword!")
    time.sleep(2)
    chrome.find_element(By.XPATH, button).click()
    time.sleep(2)
    chrome.get("https://the-internet.herokuapp.com")


service = webdriver.chrome.service.Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=service)
chrome.maximize_window()
chrome.get("https://www.techlistic.com/p/selenium-practice-form.html")
chrome.find_element(By.ID, "ez-accept-all").click()
time.sleep(5)
chrome.find_element(By.CSS_SELECTOR, "#cookieChoiceDismiss").click()
chrome.find_element(By.NAME, "firstname").send_keys("Popescu")
time.sleep(2)
chrome.find_element(By.NAME, "lastname").send_keys("Ion")
gender_list = chrome.find_elements(By.NAME, "sex")
gender_list[0].click()
time.sleep(2)
chrome.find_element(By.ID, "exp-0").click()
chrome.find_element(By.ID, "datepicker").send_keys("26.01.2023")
time.sleep(2)
chrome.find_element(By.XPATH, '//input[starts-with(@value, "Automation")]').click()
time.sleep(1)
chrome.find_element(By.XPATH, '//input[contains(@value, "Webdriver")]').click()
time.sleep(1)
dropdown_list = Select(chrome.find_element(By.CLASS_NAME, "input-xlarge"))
dropdown_list.select_by_visible_text("Europe")
time.sleep(1)
command_list = chrome.find_elements(By.XPATH, '//select[@class="input-xlarge"]')
dropdown_list = Select(command_list[1])
dropdown_list.select_by_visible_text("WebElement Commands")
time.sleep(1)
chrome.find_element(By.PARTIAL_LINK_TEXT, "Next  >>").click()
time.sleep(2)
chrome.back()
chrome.find_element(By.PARTIAL_LINK_TEXT, "Automate Upload").click()
time.sleep(2)
chrome.back()
time.sleep(2)
chrome.find_element(By.PARTIAL_LINK_TEXT, "What is Actions Class in Selenium?").click()
time.sleep(2)
chrome.back()
chrome.find_element(By.CSS_SELECTOR, "button[class^='btn']").click()
time.sleep(2)

chrome.get("https://the-internet.herokuapp.com/")
chrome.find_element(By.LINK_TEXT, "A/B Testing").click()
time.sleep(2)
chrome.back()
time.sleep(2)
chrome.find_element(By.LINK_TEXT, "Add/Remove Elements").click()
time.sleep(2)
chrome.find_element(By.TAG_NAME, "button").click()
time.sleep(2)
chrome.find_element(By.XPATH, "//*[@class='added-manually']").click()
time.sleep(2)
chrome.back()
time.sleep(2)
chrome.find_element(By.LINK_TEXT, "Entry Ad").click()
chrome.find_element(By.TAG_NAME, "p").click()
time.sleep(2)
chrome.back()
time.sleep(2)
chrome.find_element(By.XPATH, "//a[text()='Form Authentication']").click()
time.sleep(2)
chrome.find_element(By.XPATH, "//input[@id='username' and @name='username']").send_keys("tomsmith")
time.sleep(2)
chrome.find_element(By.XPATH, "//label[text()='Password']/following-sibling::input").send_keys("SuperSecretPassword!")
chrome.find_element(By.CSS_SELECTOR, ".fa.fa-2x.fa-sign-in").click()
time.sleep(2)
chrome.find_element(By.XPATH, "//i[@class='icon-2x icon-signout']/parent::a").click()
time.sleep(2)
chrome.execute_script("window.history.go(-3)")
time.sleep(2)
chrome.find_element(By.XPATH, "//a[text()='Dynamic Loading']").click()
time.sleep(2)
chrome.find_element(By.XPATH,
                    "a[href='/dynamic_loading/1'] | //a[text()='Example 1: Element on page that is hidden']").click()
time.sleep(2)
chrome.find_element(By.TAG_NAME, "button").click()
time.sleep(6)
chrome.execute_script("window.history.go(-2)")
time.sleep(2)
chrome.find_element(By.CSS_SELECTOR, "a[href='/forgot_password']").click()
time.sleep(2)
chrome.find_element(By.CSS_SELECTOR, "#email").send_keys("iforgotmypassword@gmail.com")
time.sleep(2)
chrome.find_element(By.CLASS_NAME, "radius").click()
time.sleep(2)
chrome.execute_script("window.history.go(-2)")
time.sleep(2)
chrome.find_element(By.CSS_SELECTOR, "a[href='/inputs']").click()
time.sleep(2)
chrome.find_element(By.CLASS_NAME, "example").find_element(By.TAG_NAME, "input").send_keys("31012023")
time.sleep(2)
chrome.back()
time.sleep(2)

# login using default values
login()

# login using following
# Syntax: //tagname[@attribute='value']//following::tagname
login('//div[@class="large-6 small-12 columns"]//following::input[@id="username"]',
      '//div[@class="large-6 small-12 columns"]//following::input[@id="password"]',
      '//div[@class="large-6 small-12 columns"]//following::button')

# login using following-sibling
# syntax: //tagname[@attribute='value']//following-sibling::tagname
login("//label[text()='Username']//following-sibling::input[1]",
      "//label[text()='Password']//following-sibling::input[1]",
      "//div[@class='row']//following-sibling::button")

# login using child
# syntax: //tagname[@attribute='value']//child::tagname
login("//div[@class='row']//child::input[@id='username']",
      "//div[@class='row']//child::input[@id='password']",
      "//div[@class='row']//child::button")

# login using starts-with
# syntax: //tagname[starts-with(@attribute, 'value')]
login("//input[starts-with(@type, 'text')]",
      "//input[starts-with(@type, 'pass')]",
      "//button[starts-with(@type, 'submit')]")

# login using contains
# syntax: //tagname[contains(@attribute, 'value')]
login("//input[contains(@id, 'user')]",
      "//input[contains(@id, 'pass')]",
      "//button[contains(@type, 'submit')]")


chrome.quit()
