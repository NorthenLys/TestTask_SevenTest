import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://www.seventest.com/"

@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

class TestMainPage():

    def test_main_page_switch_forum_page(self,browser):
        browser.get(link)
        forum = browser.find_element(By.CSS_SELECTOR, "a.mainmenu>:nth-child(1)")
        forum.click()
        print("test_main_page_switch_to_forum finish")
