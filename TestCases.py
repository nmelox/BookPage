import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TestCases(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.bookdepository.com/")
        self.driver.maximize_window()

    def test_search_book(self):
        self.driver.find_element_by_name("searchTerm").send_keys("Herr Pep")
        self.driver.find_element_by_name("searchTerm").send_keys(Keys.ENTER)
        element = WebDriverWait(self.driver, 100).until(
            EC.presence_of_all_elements_located((By.NAME, "searchSortBy")))
        select = Select(self.driver.find_element_by_xpath("/html/body/div[4]/div[5]/div[2]/div[2]/div[2]/form/select"))
        select.select_by_visible_text("Price, low to high")
        """orderBy = self.driver.find_element_by_name("searchSortBy")
        for option in orderBy.find_elements_by_tag_name("option"):
            if option.text == "Price, low to high":
                option.click()"""
        element = WebDriverWait(self.driver, 100).until(
            EC.presence_of_all_elements_located((By.ID,"filterLang")))
        filterLang = self.driver.find_element_by_name("searchLang")
        for option in filterLang.find_elements_by_tag_name("option"):
            if option.text == '       Spanish (3)':
                option.click()
        self.driver.find_element_by_xpath("/html/body/div[4]/div[5]/div[1]/div[1]/div/form/div[6]/button").click()
        element = WebDriverWait(self.driver,10).until(
            EC.presence_of_all_elements_located((By.LINK_TEXT,"ARS$695,37")))


    def tearDown(self):
        self.driver.get_screenshot_as_file("book.png")
        self.driver.close()
        self.driver.quit()
