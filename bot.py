from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import  UnexpectedAlertPresentException

import json

NAME = 'ROOTS'
SIZE = 'Medium'

with open('config.json') as f:
    config = json.load(f)
driver = webdriver.Chrome('../utils/chromedriver')
wait = WebDriverWait(driver, 6)


try:
    driver.get('https://ca.octobersveryown.com/collections/new-arrivals')
    items = driver.find_elements_by_css_selector('.h6 a')

    input("SELECT YOUT ITEM AND PRESS ENTER")

    """
    # Search for item in new-arrivals
    search_results = []
    for item in items:
        if NAME in item.text:
            search_results.append(item)
    # Do length test
    search_results[0].click()
    """

    size = wait.until(EC.presence_of_element_located((By.ID, 'productSelect')))
    size_options = size.find_elements_by_tag_name("option")
    for optn in size_options:
        print(optn.text)
        if optn.text.startswith(SIZE):
            size_text = optn.text
            break
    select = Select(size)
    select.select_by_visible_text(size_text)

    add_cart = driver.find_element_by_id('AddToCartText')
    add_cart.click()

    # Ok
    # If {Alert text : Cannot place order, conditions not met: } pops up
    try:
        agree = wait.until(EC.presence_of_element_located((By.ID, 'agree_box')))
        agree.click()
        checkout = driver.find_element_by_name('checkout')
        checkout.click()
    except UnexpectedAlertPresentException:
        input("Unexpected pop up. Press enter to continue")
        pass

    # Add information
    info = config['info']
    email = wait.until(EC.presence_of_element_located((By.ID, 'checkout_email')))
    email.send_keys(info['email'])
    # driver.find_element_by_id('checkout_email').send_keys(email)
    driver.find_element_by_id('checkout_shipping_address_first_name').send_keys(info['first_name'])
    driver.find_element_by_id('checkout_shipping_address_last_name').send_keys(info['last_name'])
    driver.find_element_by_id('checkout_shipping_address_city').send_keys(info['city'])
    driver.find_element_by_id('checkout_shipping_address_address1').send_keys(info['address'])
    driver.find_element_by_id('checkout_shipping_address_phone').send_keys(info['phone'])
    driver.find_element_by_id('checkout_shipping_address_zip').send_keys(info['zip'])
    WAITFORCAPTCHA = input("SOLVE CAPTCHA AND PRESS ANY KEY")
    driver.find_element_by_css_selector('.step__footer__continue-btn').click()

    # Shipping method
    continue_to_payment = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.step__footer__continue-btn')))
    continue_to_payment.click()

    # Payment method
    payment = config['payment']
    cards_frame = driver.find_element_by_class_name('card-fields-iframe')
    driver.switch_to.frame(cards_frame)

    cc_number = wait.until(EC.presence_of_element_located((By.ID, 'number')))
    cc_number.send_keys(payment['card_number'])
    cc_name = wait.until(EC.element_to_be_clickable((By.ID,'name')))
    cc_name.click()
    cc_name.send_keys(payment['card_name'])
    # driver.find_element_by_id('name')
    driver.find_element_by_id('expiry').send_keys(payment['card_expiry'])
    driver.find_element_by_id('verification_value').send_keys(payment['card_ccv'])
    driver.find_element_by_css_selector('.step__footer__continue-btn').click()
# except KeyboardInterrupt:
#     exit()
except Exception as e:
    input('Got exception')
    raise e
input()

exit()

# driver.get('https://ca.octobersveryown.com/collections/shop-all')


# s_len = len(driver.find_elements_by_css_selector('.search-bar .input-group-field'))
# driver.find_elements_by_css_selector('.search-bar .input-group-field')[s_len-1].send_keys('test')

"""
search = wait.until(EC.visibility_of((By.CSS_SELECTOR, '.search-bar .input-group-field')))
print(search)
search[0].click()
search.send_keys('OG Hoodie')

input()
driver.close()


ok_size = driver.findElements(By.xpath("//button[text()='OK']")).size();

driver.findElements(By.xpath("//button[text()='OK']")).get(ok_size - 1).click();

"""
