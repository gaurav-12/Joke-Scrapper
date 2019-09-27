from selenium import webdriver as driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url = "http://123hindijokes.com/very-funny-jokes/"
browser = driver.Chrome()
browser.get(url)

with open("jokes.txt", "w", encoding="utf-8") as jFile:
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "ul.statusList"))
    )

    pagesLinks = browser.find_element_by_class_name("page-links").find_elements_by_tag_name("a")

    for i in range(len(pagesLinks)-1):
        jokes = browser.find_element_by_css_selector("ul.statusList").find_elements_by_tag_name("li")

        for j in jokes:
            jFile.write('"' + j.text + '",\n')

        pagesLinks[i].click()
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "ul.statusList"))
        )
        pagesLinks = browser.find_element_by_class_name("page-links").find_elements_by_tag_name("a")


browser.quit()





