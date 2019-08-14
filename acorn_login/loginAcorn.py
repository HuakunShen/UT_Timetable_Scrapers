from selenium import webdriver
from password import ACORN_USERNAME
from password import ACORN_PASSWORD
import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('https://www.acorn.utoronto.ca/')
time.sleep(1)
browser.find_element_by_css_selector('a[href="https://acorn.utoronto.ca/"]').click()
time.sleep(1)
username = browser.find_element_by_id("username")
username.send_keys(ACORN_USERNAME)
password = browser.find_element_by_id('password')
password.send_keys(ACORN_PASSWORD)
password.send_keys(Keys.ENTER)
time.sleep(1)
browser.find_element_by_css_selector("a[href='#/courses']").click()
time.sleep(1)
browser.find_element_by_css_selector("a[href='#/courses/1']").click()
time.sleep(1)
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
time.sleep(1)
courseBox = browser.find_elements_by_css_selector(".coursePlan.courseBox")
targetCourse = courseBox[-1]
a_links = targetCourse.find_elements_by_css_selector("a")
enrol_btn = a_links[2]
enrol_btn.click()
time.sleep(1)
enrol_btn = browser.find_element_by_css_selector('#enrolFromPlan')
time.sleep(1)
enrol_btn.click()
