from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from infofile import *

class InstaBot:
    def __init__(self, username, pw, targetaccount, targetpost, taglist):
        self.driver = webdriver.Chrome('/usr/bin/chromedriver')
        self.username = username
        self.pw = pw
        self.targetaccount = targetaccount
        self.targetpost = targetpost
        self.taglist = taglist

        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(text(), 'Log in')]")\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')\
            .send_keys(targetaccount)
        sleep(2)
        clickmessage = "//a[@href='/%s/']" % targetaccount
        self.driver.find_element_by_xpath(clickmessage)\
            .click()
        sleep(2)
        clickmessage = "//a[@href='/%s/']" % targetpost
        self.driver.find_element_by_xpath(clickmessage)\
            .click()
        sleep(4)

        for tag in taglist:
            self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea')\
                .click()
            sleep(2)
            self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea')\
                .send_keys(tag)
            sleep(2)
            self.driver.find_element_by_xpath('//button[@type="submit"]')\
                .click()
            sleep(4)


my_bot = InstaBot(username, pw, accountname, post, taglist)