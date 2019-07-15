from threading import Thread
import mysql.connector
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

sql = "INSERT INTO `degrees` (`ID`, `Name`, `rakamglos`, `school`, `edara`, `status`, `kam_mada`, `sho3ba`, `Arabic`, `English`, `SecLanguage`, `Math2`, `History`, `Geo`, `Falsfa`, `Nafs`, `Kemya`, `Ahyaa`, `Geologya`, `MathTabe2`, `Physics`, `Total`, `Nesba`) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"


class myClassA(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
    def run(self):
        Number1 = 220600
        while True:
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="123456789",
                    database="thanwyascrape"
                )
                mycursor1 = mydb.cursor()

                driver = webdriver.Chrome()
                driver.get("http://natega2.youm7.com/")
                inputElement = driver.find_element_by_id("seating_no")
                for c in str(Number1):
                    # print(c)
                    inputElement.send_keys(c)

                inputElement2 = driver.find_element_by_id("submit")
                inputElement2.click()

                firstcategory = driver.find_elements_by_css_selector(".full-result li span:not(.nav-link)")
                secondcategory = driver.find_elements_by_css_selector(".result-details li .formatt4")
                nesba = driver.find_elements_by_css_selector(".halfinput-result li h1:not(.format3)")[2]



                val = (
                firstcategory[0].get_attribute('innerHTML')
                , Number1
                , firstcategory[1].get_attribute('innerHTML')
                , firstcategory[2].get_attribute('innerHTML')
                , firstcategory[4].get_attribute('innerHTML')
                , firstcategory[3].get_attribute('innerHTML')
                , firstcategory[6].get_attribute('innerHTML')
                , secondcategory[0].get_attribute('innerHTML')
                , secondcategory[1].get_attribute('innerHTML')
                , secondcategory[2].get_attribute('innerHTML')
                , secondcategory[3].get_attribute('innerHTML')
                , secondcategory[4].get_attribute('innerHTML')
                , secondcategory[5].get_attribute('innerHTML')
                , secondcategory[6].get_attribute('innerHTML')
                , secondcategory[7].get_attribute('innerHTML')
                , secondcategory[8].get_attribute('innerHTML')
                , secondcategory[9].get_attribute('innerHTML')
                , secondcategory[10].get_attribute('innerHTML')
                , secondcategory[11].get_attribute('innerHTML')
                , secondcategory[12].get_attribute('innerHTML')
                , secondcategory[13].get_attribute('innerHTML')
                , nesba.get_attribute('innerHTML'))
                mycursor1.execute(sql, val)
                print("1 record inserted, ID:", mycursor1.lastrowid)
                mydb.commit()

                print(Number1)
                Number1 = Number1 + 2

                driver.close()
            except:
                driver.close()
                print ("This is an error message!")


class myClassB(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
    def run(self):
        Number2 = 220601
        while True:
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="123456789",
                    database="thanwyascrape"
                )
                mycursor2 = mydb.cursor()


                driver = webdriver.Chrome()
                driver.get("http://natega2.youm7.com/")
                inputElement = driver.find_element_by_id("seating_no")
                for c in str(Number2):
                    # print(c)
                    inputElement.send_keys(c)

                inputElement2 = driver.find_element_by_id("submit")
                inputElement2.click()



                firstcategory = driver.find_elements_by_css_selector(".full-result li span:not(.nav-link)")
                secondcategory = driver.find_elements_by_css_selector(".result-details li .formatt4")
                nesba = driver.find_elements_by_css_selector(".halfinput-result li h1:not(.format3)")[2]



                val = (
                firstcategory[0].get_attribute('innerHTML')
                , Number2
                , firstcategory[1].get_attribute('innerHTML')
                , firstcategory[2].get_attribute('innerHTML')
                , firstcategory[4].get_attribute('innerHTML')
                , firstcategory[3].get_attribute('innerHTML')
                , firstcategory[6].get_attribute('innerHTML')
                , secondcategory[0].get_attribute('innerHTML')
                , secondcategory[1].get_attribute('innerHTML')
                , secondcategory[2].get_attribute('innerHTML')
                , secondcategory[3].get_attribute('innerHTML')
                , secondcategory[4].get_attribute('innerHTML')
                , secondcategory[5].get_attribute('innerHTML')
                , secondcategory[6].get_attribute('innerHTML')
                , secondcategory[7].get_attribute('innerHTML')
                , secondcategory[8].get_attribute('innerHTML')
                , secondcategory[9].get_attribute('innerHTML')
                , secondcategory[10].get_attribute('innerHTML')
                , secondcategory[11].get_attribute('innerHTML')
                , secondcategory[12].get_attribute('innerHTML')
                , secondcategory[13].get_attribute('innerHTML')
                , nesba.get_attribute('innerHTML'))
                mycursor2.execute(sql, val)
                print("1 record inserted, ID:", mycursor2.lastrowid)
                mydb.commit()
                print(Number2)
                Number2 = Number2 + 2
                driver.close()

            except:
                driver.close()

                print
                "This is an error message!"



myClassA()
myClassB()

while True:
    pass