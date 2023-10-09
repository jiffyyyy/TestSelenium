from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import unittest

class ViewInformation(unittest.TestCase):

    def setUp(self):
        # Initialize the Chrome WebDriver
        s = Service('D:\webdriver\chromedriver.exe')
        self.driver = webdriver.Chrome(service=s)

    def tearDown(self):
        # Close the browser
        self.driver.quit()

    def test_information(self):
        # Open the web application
        self.driver.get("https://online-web-mauve.vercel.app/")
        
        icon = self.driver.find_element(By.ID, 'Home-medical')
        icon.click()
        time.sleep(4)

        link_element = self.driver.find_element(By.XPATH, "//a[@class='btn btn-primary mx-1' and @href='/detaildental/1']")
        link_element.click()
        time.sleep(3)


        Back = self.driver.find_element(By.ID, "BackshowdepartmentAll")
        Back.click()
        time.sleep(3)


        link_element = self.driver.find_element(By.XPATH, "//a[@class='btn btn-primary mx-1' and @href='/detaildental/2']")
        link_element.click()
        time.sleep(3)


        Back = self.driver.find_element(By.ID, "BackshowdepartmentAll")
        Back.click()
        time.sleep(3)


        link_element = self.driver.find_element(By.XPATH, "//a[@class='btn btn-primary mx-1' and @href='/detaildental/3']")
        link_element.click()
        time.sleep(3)


        Back = self.driver.find_element(By.ID, "BackshowdepartmentAll")
        Back.click()
        time.sleep(3)

        link_element = self.driver.find_element(By.XPATH, "//a[@class='btn btn-primary mx-1' and @href='/detaildental/4']")
        link_element.click()
        time.sleep(3)


        Back = self.driver.find_element(By.ID, "BackshowdepartmentAll")
        Back.click()
        time.sleep(3)

        # เลื่อนหน้าเว็บมายัง Element 'New'
        new_element = self.driver.find_element(By.XPATH, '//*[@id="detaildental"]/h4')
        self.driver.execute_script("arguments[0].scrollIntoView();", new_element)
        time.sleep(2)  # รอสักครู่ให้หน้าเว็บเลื่อนมา

        link_element = self.driver.find_element(By.XPATH, "//a[@class='btn btn-primary mx-1' and @href='/detaildental/6']")
        link_element.click()
        time.sleep(3)

        # เลื่อนหน้าเว็บขึ้นข้างบน
        self.driver.execute_script("window.scrollBy(0, -1000);")
        time.sleep(2)  # รอสักครู่ให้หน้าเว็บเลื่อน

        Back = self.driver.find_element(By.ID, "BackshowdepartmentAll")
        Back.click()
        time.sleep(3)
        # เลื่อนหน้าเว็บมายัง Element 'New'
        new_element = self.driver.find_element(By.XPATH, '//*[@id="detaildental"]/h4')
        self.driver.execute_script("arguments[0].scrollIntoView();", new_element)
        time.sleep(2)  # รอสักครู่ให้หน้าเว็บเลื่อนมา


        link_element = self.driver.find_element(By.XPATH, "//a[@class='btn btn-primary mx-1' and @href='/detaildental/7']")
        link_element.click()
        time.sleep(3)
        # เลื่อนหน้าเว็บขึ้นข้างบน
        self.driver.execute_script("window.scrollBy(0, -1000);")
        time.sleep(2)  # รอสักครู่ให้หน้าเว็บเลื่อน

        Back = self.driver.find_element(By.ID, "BackshowdepartmentAll")
        Back.click()
        time.sleep(3)

        # เลื่อนหน้าเว็บมายัง Element 'New'
        new_element = self.driver.find_element(By.XPATH, '//*[@id="detaildental"]/h4')
        self.driver.execute_script("arguments[0].scrollIntoView();", new_element)
        time.sleep(2)  # รอสักครู่ให้หน้าเว็บเลื่อนมา

        link_element = self.driver.find_element(By.XPATH, "//a[@class='btn btn-primary mx-1' and @href='/detaildental/8']")
        link_element.click()
        time.sleep(3)
        
        # เลื่อนหน้าเว็บขึ้นข้างบน
        self.driver.execute_script("window.scrollBy(0, -1000);")
        time.sleep(2)  # รอสักครู่ให้หน้าเว็บเลื่อน


        Back = self.driver.find_element(By.ID, "BackshowdepartmentAll")
        Back.click()
        time.sleep(3)

        # เลื่อนหน้าเว็บมายัง Element 'New'
        new_element = self.driver.find_element(By.XPATH, '//*[@id="detaildental"]/h4')
        self.driver.execute_script("arguments[0].scrollIntoView();", new_element)
        time.sleep(2)  # รอสักครู่ให้หน้าเว็บเลื่อนมา

        link_element = self.driver.find_element(By.XPATH, "//a[@class='btn btn-primary mx-1' and @href='/detaildental/23']")
        link_element.click()
        time.sleep(3)
        # เลื่อนหน้าเว็บขึ้นข้างบน
        self.driver.execute_script("window.scrollBy(0, -1000);")
        time.sleep(2)  # รอสักครู่ให้หน้าเว็บเลื่อน


        Back = self.driver.find_element(By.ID, "BackshowdepartmentAll")
        Back.click()
        time.sleep(3)



        img_element = self.driver.find_element(By.ID, 'HospitalLogo.17')  # หรือใช้ By.CLASS_NAME หรือวิธีการค้นหาอื่น ๆ

        img_element.click()
        time.sleep(3)

    def test_view_news(self):
        self.driver.get("https://online-web-mauve.vercel.app/")

       # เลื่อนหน้าเว็บมายัง Element 'NewsS'
        new_element = self.driver.find_element(By.ID, 'NewsS')
        self.driver.execute_script("arguments[0].scrollIntoView();", new_element)
        time.sleep(2)  # รอสักครู่ให้หน้าเว็บเลื่อนมา

    # คลิกที่ Element 'Newsdentalservice'
        element = self.driver.find_element(By.ID, "Newsdentalservice")
        element.click()
        time.sleep(5)

    # คลิกที่โลโก้ของโรงพยาบาล
        Logo = self.driver.find_element(By.ID,"HospitalLogo.17")
        Logo.click()
        time.sleep(5)

    # เลื่อนหน้าเว็บมายัง Element 'NewsS' อีกครั้ง
        new_element = self.driver.find_element(By.ID, 'NewsS')
        self.driver.execute_script("arguments[0].scrollIntoView();", new_element)
        time.sleep(2)

    # คลิกที่ Element 'Newsfluvaccine'
        element = self.driver.find_element(By.ID, "Newsfluvaccine")
        element.click()
        time.sleep(5)

    # คลิกที่โลโก้ของโรงพยาบาล
        Logo = self.driver.find_element(By.ID, "HospitalLogo.17")
        Logo.click()
        time.sleep(5)

    # เลื่อนหน้าเว็บมายัง Element 'NewsS' อีกครั้ง
        new_element = self.driver.find_element(By.ID, 'NewsS')
        self.driver.execute_script("arguments[0].scrollIntoView();", new_element)
        time.sleep(2)

    # คลิกที่ Element 'NewsModernaBivalent'
        element = self.driver.find_element(By.ID, "NewsModernaBivalent")
        element.click()
        time.sleep(5)

    # คลิกที่โลโก้ของโรงพยาบาล
        Logo = self.driver.find_element(By.ID, "HospitalLogo.17")
        Logo.click()
        time.sleep(5)

    # เลื่อนหน้าเว็บมายัง Element 'NewsfoodN'
        new_element = self.driver.find_element(By.ID, 'NewsfoodN')
        self.driver.execute_script("arguments[0].scrollIntoView();", new_element)
        time.sleep(2)

    # คลิกที่ Element 'Newsfood'
        element = self.driver.find_element(By.ID, "Newsfood")
        element.click()
        time.sleep(5)

    # คลิกที่โลโก้ของโรงพยาบาล
        Logo = self.driver.find_element(By.ID, "HospitalLogo.17")
        Logo.click()
        time.sleep(2)

if __name__ == "__main__":
    unittest.main()
