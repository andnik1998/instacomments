from selenium import webdriver
from time import sleep
from empty_infofile import *
import numpy


class InstaBot:
    def __init__(self, username, pw, targetaccount, targetpost, taglist):
        self.driver = webdriver.Chrome('C:/chromedriver')
        self.username = username
        self.pw = pw
        self.targetaccount = targetaccount
        self.targetpost = targetpost
        self.taglist = taglist

        # all sleep() uses are to compensate for the buffering while content is loading

        # Visits instagram website and logs in with given account
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]") \
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]") \
            .send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]') \
            .click()
        sleep(4)

        # Closes popup asking to add instagram to your homescreen
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]") \
            .click()
        sleep(2)

        # Closes popup asking to add instagram to your homescreen
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]") \
            .click()
        sleep(2)

        # Searches for account given in parameters and clicks of their profile
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input') \
            .send_keys(targetaccount)
        sleep(2)
        clickmessage = "//a[@href='/%s/']" % targetaccount
        self.driver.find_element_by_xpath(clickmessage) \
            .click()
        sleep(2)

        # Clicks on the post given in the parameters
        clickmessage = "//a[@href='/%s/']" % targetpost
        self.driver.find_element_by_xpath(clickmessage) \
            .click()
        sleep(4)

        # THREE TAGS PER COMMENT

        for i in range(71, 90):
            self.driver.find_element_by_xpath(
                '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea') \
                .click()
            sleep(2)
            tempcomment = taglist[i][0] + " " + taglist[i][1]
            self.driver.find_element_by_xpath(
                '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea') \
                .send_keys(tempcomment)
            sleep(2)
            self.driver.find_element_by_xpath('//button[@type="submit"]') \
                .click()
            sleep(numpy.random.randint(2, 20))
            print(i)

        # for i in taglist:
        #     iternum = len(i)
        #     for j in range(0, iternum, len(i)):
        #         tempcomment = ''
        #         self.driver.find_element_by_xpath(
        #             '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea') \
        #             .click()
        #         sleep(2)
        #         for k in range(len(i)):
        #             tempcomment += i[k] + " "
        #         tempcomment = tempcomment[:-1]
        #         self.driver.find_element_by_xpath(
        #             '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea') \
        #             .send_keys(tempcomment)
        #         sleep(2)
        #         self.driver.find_element_by_xpath('//button[@type="submit"]') \
        #             .click()
        #         sleep(2)
        #     sleep(numpy.random.randint(2, 30))


# initialise instance of bot object
my_bot = InstaBot(username, pw, accountname, post, taglist)
