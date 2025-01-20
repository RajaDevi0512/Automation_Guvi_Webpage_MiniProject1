
from pageObject.LoginPage import GUVI_Automation


# To validate the URL
def test_validate_URL(): #test 1
    assert GUVI_Automation().start() == 'https://www.guvi.in/'
    print('URL Check!!')
    # GUVI_Automation().Invalid_login()

# To validate the Title
def test_validateTitle(): #test2
    # assert GUVI_Automation().get_title() =='GUVI | Learn to code in your native language'| "GUVI | Login"
    assert GUVI_Automation().get_title() == "GUVI | Learn to code in your native language"
    print('Title check!!')
    # print(GUVI_Automation().login())

# To validate the Login button visibility
def test_login_button_visibility(): #test3
    # Instantiate the class with driver
    assert GUVI_Automation().login_button_visibility() == "Login"
    print("Login button visible")

# To validate the Signup button visibility   
def test_signup_button_visibility(): #test5
    # Instantiate the class with driver
    assert GUVI_Automation().signup_button_visibility() == "Sign up"
    print("Signup button visible")

# To validate the Login button clickablity
def test_login_button_clickable(): #test4
   assert GUVI_Automation().login_button_clickability() == "https://www.guvi.in/sign-in/"
   print("Login button visible")
 
# To validate the Signup button clickability
def test_signup_button_clickable(): #test6
   assert GUVI_Automation().signup_button_clickability() == "https://www.guvi.in/register/"
   print("signup button visible")

# To validate the Valid credentials
def test_Valid_login(): #test7
    assert GUVI_Automation().Valid_login() == 'https://www.guvi.in/courses/?current_tab=myCourses' 
    print("SUCCESS: Logged In!")
   
# To validate the Logout
def test_logout(): #test8
    assert GUVI_Automation().logout() == 'https://www.guvi.in/'
    print("SUCCESS: logged out")

# To validate the Login with Invalid credentials
def test_InValid_login(): #test9
    assert GUVI_Automation().Invalid_login() == "Incorrect Email or Password"
    print("Failed: Wrong Credentials!")

# To validate the shutdown
def test_shutdown(): #test9
    assert GUVI_Automation().shutdown() == None
    print("SUCCEESS: Automation completed!!")