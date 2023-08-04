from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_has_buy_option(browser):
    browser.get(link)
    assert browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")