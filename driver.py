import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import students

options = Options()
options.page_load_strategy = 'normal'
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(15)

def validateTags(tags, url):
    points = 0
    driver.get(url)
    driver.fullscreen_window()
    #image = driver.get_screenshot_as_png()
    possible_points = 0
    for tag in tags:
        possible_points += 1
        all_tags = driver.find_elements(By.TAG_NAME, tag)
        if len(all_tags) == 0:
            print("missing " + tag + " tag");
        else:
            count = 0
            for t in all_tags:
                count += 1
            if count >= tags[tag]:
                points += 1
    return (points, possible_points)

def goToCanvas(results):
    driver.get("https://ccsdut.instructure.com/courses/71819/gradebook")
    username = driver.find_element(By.ID, "pseudonym_session_unique_id")
    username.send_keys("andruss")
    password = driver.find_element(By.ID, "pseudonym_session_password")
    password.send_keys("The@Burrita19")
    password.submit()
    time.sleep(10)
    assignment_filter = driver.find_element(By.ID, "assignments-filter")
    assignment_filter.send_keys("Heading Element Assignment")
    assignment_filter.send_keys(Keys.ENTER)
    for result in results:
        name_filter = driver.find_element(By.ID, "student-names-filter")
        name = students[result]
        name_filter.send_keys(name)
        name_filter.send_keys(Keys.ENTER)

    input()