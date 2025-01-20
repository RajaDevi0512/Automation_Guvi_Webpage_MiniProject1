'''
Login page contains all elements related to login page only.

This is a page object file
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import Chrome
from time import sleep # for login url fetching

from testData.Data import GUVI_data
from testLocator.locator import GUVI_locator

from selenium.webdriver.common.action_chains import ActionChains

    # import the webdriver wait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

    #import exceptions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import ElementClickInterceptedException
from  selenium.common.exceptions import TimeoutException

class GUVI_Automation:
               
    driver = webdriver.Chrome()
    ignored_exceptions = [NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException, TimeoutException]
    wait = WebDriverWait(driver, 50, poll_frequency=5, ignored_exceptions=ignored_exceptions)

    # URL Chcek
    def start(self):
        self.driver.maximize_window()
        # self.driver.implicitly_wait(20)
        self.driver.get(GUVI_data.url)
        url_check = self.driver.current_url
        return url_check
    
    # Title Chcek
    def get_title(self):
        guvi_title = self.driver.title
        return guvi_title
    
    # Login Button Visibility Check
    def login_button_visibility(self):
        login_text = self.driver.find_element(by=By.XPATH, value= GUVI_locator.loginIcon_locator ).text
        # print(login_text)
        return login_text
    
    # Signup Button Visibility Check
    def signup_button_visibility(self):
        signup_text = self.driver.find_element(by=By.XPATH, value= GUVI_locator.signUp_locator ).text
        # print(signup_text)
        return signup_text 
    
    # Login Button Clickability Check
    def login_button_clickability(self):
        self.driver.find_element(by=By.XPATH, value= GUVI_locator.loginIcon_locator).click()
        self.driver.refresh()
        login_url = self.driver.current_url
        self.driver.back()
        # print(login_url)
        return login_url
        
    # Signup Button Clickability Check    
    def signup_button_clickability(self):
        self.driver.find_element(by=By.XPATH, value= GUVI_locator.signUp_locator).click()
        self.driver.refresh()
        signup_url = self.driver.current_url
        self.driver.back()
        # print(signup_url)
        return signup_url

    # Login using valid credentials
    def Valid_login(self):
        
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, GUVI_locator.loginIcon_locator))).click()
            # print("Login_icon locator")
    
            self.wait.until(EC.presence_of_element_located((By.XPATH, GUVI_locator.userName_locator))).send_keys(GUVI_data.Valid_userName)
            # print("Username")
    
            self.wait.until(EC.presence_of_element_located((By.XPATH,GUVI_locator.password_locator))).send_keys(GUVI_data.Valid_password)
            # print("Password")
              
            self.wait.until(EC.element_to_be_clickable((By.ID,GUVI_locator.login_locator))).click()
            # print("Login button")
            sleep(5) # for login url fetching
            # self.driver.refresh()
            dashboard_url = self.driver.current_url
            return dashboard_url
            
                   
        except (NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException, TimeoutException) as error:
            print(error)
            return False

    # Login using Invalid credentials 
    def Invalid_login(self):
        
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, GUVI_locator.loginIcon_locator))).click()
            # print("Login_icon locator")
            sleep(2)
            self.wait.until(EC.presence_of_element_located((By.XPATH, GUVI_locator.userName_locator))).send_keys(GUVI_data.InValid_userName)
            # print("Username")
    
            self.wait.until(EC.presence_of_element_located((By.XPATH,GUVI_locator.password_locator))).send_keys(GUVI_data.INValid_password)
            # print("Password")
              
            self.wait.until(EC.element_to_be_clickable((By.ID,GUVI_locator.login_locator))).click()
            # print("Login button")
            sleep(2)
            error_message = self.driver.find_element(By.XPATH, GUVI_locator.error_message_locator).text
            sleep(2)
            # print (error_message)
            # self.driver.refresh()
            return error_message
                   
        except (NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException, TimeoutException) as error:
            print(error)
            return False

    #Logout function check 
    def logout(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Later']"))).click() # handling the Pop-up message that occurs randomly
            # Wait for the logout icon and click
            self.wait.until(EC.element_to_be_clickable((By.XPATH, GUVI_locator.logout_locator))).click()
            # print("Found Log out icon")
            sleep(2)
            
            # Wait for the sign-out option to be visible and click
            self.wait.until(EC.visibility_of_element_located((By.XPATH, GUVI_locator.Sign_out))).click()
            # print("Logged out successfully")
            sleep(2)

            # Refresh the page to ensure we're at the correct URL after logout
            self.driver.refresh()
            sleep(2)
            
            # Capture the current URL after logging out
            logout_url = self.driver.current_url
            # print(f"Current URL after logout: {logout_url}")

            return logout_url
        
        except (NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException, TimeoutException) as error:
            print(f"Error during logout: {error}")
            return None 

       
    # Shutting down the browser
    def shutdown(self):
        self.driver.quit()
        return None