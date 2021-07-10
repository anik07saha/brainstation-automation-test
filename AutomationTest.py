from selenium import webdriver
from time import sleep
import unittest
import HtmlTestRunner


class PhpTravels(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='../drivers/chromedriver')
        cls.driver.maximize_window()

    def test_01_home_page(self):
        self.driver.get('https://www.phptravels.net/home')
        self.driver.implicitly_wait(5)

    def test_02_tours(self):
        self.driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/nav[1]/ul[1]/li[5]/a[1]").click()
        sleep(2)

    def test_03_search_by_elements(self):
        self.driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/a[1]/span[1]").click()
        self.driver.find_element_by_xpath("/html[1]/body[1]/div[7]/div[1]/input[1]").send_keys("Legoland Malaysia Day Pass")
        sleep(2)
        self.driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/form[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/a[1]/span[1]").click()
        self.driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/form[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/ul[1]/li[9]").click()
        sleep(2)
        self.driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/form[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/input[1]").click()
        self.driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/form[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/input[1]").click()
        sleep(2)
        self.driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/form[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/input[1]")
        sleep(2)
        self.driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/form[1]/div[1]/div[1]/div[4]/button[1]").click()
        self.driver.find_element_by_xpath("/html[1]/body[1]/brabrainstation-automation-tesdiv[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/form[1]/div[1]/div[1]/div[4]/button[1]").click()
        sleep(5)

    def test_04_book_now(self):
        self.driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/aside[1]/div[1]/form[1]/div[1]/form[1]/button[1]").click()
        sleep(2)

    def test_05_booking_as_a_guest(self):
        self.driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]/ul[1]/li[1]/a[1]").click()
        self.driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/label[1]/span[1]").send_keys("Anik")
        self.driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/label[1]/span[1]").send_keys("Saha")
        self.driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/label[1]/span[1]").send_keys("ak07saha@gmail.com")
        self.driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[1]/form[1]/div[2]/div[2]/label[1]/span[1]").send_keys("ak07saha@gmail.com")
        self.driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[1]/form[1]/div[3]/div[1]/label[1]/span[1]").send_keys("+8801676459596")
        self.driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[1]/form[1]/div[4]/div[1]/label[1]/span[1]").send_keys("House No#44, Road no#09, Nikunja 2, Khilkhet, Dhaka 1229")
        self.driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[1]/form[1]/div[5]/div[1]/div[2]/a[1]/span[1]").click()
        self.driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[1]/form[1]/div[5]/div[1]/div[2]/div[1]/div[1]").send_keys("Bangladesh")
        self.driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[1]/form[1]/div[5]/div[1]/div[2]").click()
        self.driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[9]/button[1]").click()
        sleep(5)

    def test_06_payment(self):
        self.driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/center[1]/button[1]").click()
        sleep(2)

    def test_07_sign_up(self):
        self.driver.get('https://www.phptravels.net/home')
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("/html[1]/body[1]/div[2]/header[1]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[3]/div[1]/a[1]").click()
        self.driver.find_element_by_xpath("//header/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[3]/div[1]/div[1]/div[1]/a[2]").click()
        sleep(2)
        self.driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/section[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/div[1]/div[1]/label[1]/span[1]").send_keys("Anik")
        self.driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/section[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/div[2]/div[1]/label[1]/span[1]").send_keys("Saha")
        self.driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/section[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[4]/label[1]/span[1]").send_keys("+8801676459596")
        self.driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/section[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[5]/label[1]/span[1]").send_keys("ak07saha@gmail.com")
        self.driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/section[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[6]/label[1]/span[1]").send_keys("VsXutmFgWcMp7Ve")
        self.driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/section[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[7]/label[1]/span[1]").send_keys("VsXutmFgWcMp7Ve")
        self.driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/section[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[8]/button[1]").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print("Search Done")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/user/PycharmProjects/pythonProject/reports'))
