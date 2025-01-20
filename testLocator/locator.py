'''
locator file contains all the locator such as class name, ID, Xpath
'''

class GUVI_locator:
    userName_locator = "//div[@id ='emailgroup']/input"  #XPATH
    password_locator = "//div[@id ='passwordGroup']/input"  #ID
    loginIcon_locator ="//a[@id='login-btn']"#XPATH
    login_locator = 'login-btn' #ID
    signUp_locator = '//a[contains(text(),"Sign up")]' #XPATH  
    Later_button = "startPreassess" #ID
    logout_locator = "//div[@id='dropdown_title']" #XPATH   #"/html/body/div[1]/div/div[5]/div/div[2]/div" #XPATH 2)//div[@id='accountGroup']/button
    error_message_locator =  '//div[@id="passwordGroup"]/div'     #'//div[contains(text(),"Incorrect Email or Password")]' #XPATH
    Sign_out = '//ul[@id="drop_contents"]/li[4]/div' #XPATH 
    dobby_message = 'close-fill' #ID