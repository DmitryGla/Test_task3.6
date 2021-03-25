#import time
link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_user_should_see_button(browser):
    browser.get(link)
    button = browser.find_element_by_css_selector("[type='submit']")
    assert button, "No button"
    #time.sleep(10)
