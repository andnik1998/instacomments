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

        # all sleep() uses are to compensate for the buffering while content is loading

        # Visits instagram website and logs in with given account
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

        # Closes popup asking to add instagram to your homescreen
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        sleep(2)

        # Searches for acount given in parameters and clicks of their profile
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')\
            .send_keys(targetaccount)
        sleep(2)
        clickmessage = "//a[@href='/%s/']" % targetaccount
        self.driver.find_element_by_xpath(clickmessage)\
            .click()
        sleep(2)

        # Clicks on the post given in the parameters
        clickmessage = "//a[@href='/%s/']" % targetpost
        self.driver.find_element_by_xpath(clickmessage)\
            .click()
        sleep(4)

        # THREE TAGS PER COMMENT
        
        # adds all tags as individual comments on the post
        iternum = len(taglist)//3 * 3
        
        for i in range(0, iternum, 3):
            tempcomment = ''
            self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea')\
                .click()
            sleep(2)
            tempcomment = taglist[i] + " " + taglist[i+1] + " " + taglist[i+2]
            self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea')\
                .send_keys(tempcomment)
            sleep(2)
            self.driver.find_element_by_xpath('//button[@type="submit"]')\
                .click()
            sleep(5)

        # ONE TAG PER COMMENT

        # adds all tags as individual comments on the post
        # for tag in taglist:
        #     self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea')\
        #         .click()
        #     sleep(2)
        #     self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea')\
        #         .send_keys(tag)
        #     sleep(2)
        #     self.driver.find_element_by_xpath('//button[@type="submit"]')\
        #         .click()
        #     sleep(4)

        

# initialise instance of bot object
my_bot = InstaBot(username, pw, accountname, post, taglist)