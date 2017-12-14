from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome('../utils/chromedriver')
wait = WebDriverWait(driver, 10)
name = 'ROOTS'
email = "adsfadsf@hotmail.com"
first_name = 'Adil'
last_name = 'Asim'
address = '485 Avens St'
city = 'Waterloo'
zip = 'N2V 0B7'
phone = '5195047798'


try:
    driver.get('https://ca.octobersveryown.com/collections/new-arrivals')
    items = driver.find_elements_by_css_selector('.h6 a')

    search_results = []
    for item in items:
        if name in item.text:
            search_results.append(item)
    # Do length test
    search_results[0].click()

    size = wait.until(EC.presence_of_element_located((By.ID, 'productSelect')))
    size_options = size.find_elements_by_tag_name("option")
    for optn in size_options:
        if optn.text.startswith('Medium'):
            size_text = optn.text
    select = Select(size)
    select.select_by_visible_text(size_text)

    add_cart = driver.find_element_by_id('AddToCartText')
    add_cart.click()

    agree = wait.until(EC.presence_of_element_located((By.ID, 'agree_box')))
    agree.click()
    checkout = driver.find_element_by_name('checkout')
    checkout.click()

    # Add information
    email = wait.until(EC.presence_of_element_located((By.ID, 'checkout_email')))
    email.send_keys(email)
    # driver.find_element_by_id('checkout_email').send_keys(email)
    driver.find_element_by_id('checkout_shipping_address_first_name').send_keys(first_name)
    driver.find_element_by_id('checkout_shipping_address_last_name').send_keys(last_name)
    driver.find_element_by_id('checkout_shipping_address_city').send_keys(city)
    driver.find_element_by_id('checkout_shipping_address_address1').send_keys(address)
    driver.find_element_by_id('checkout_shipping_address_phone').send_keys(phone)
    driver.find_element_by_id('checkout_shipping_address_zip').send_keys(zip)
    WAITFORCAPTCHA = input()
    driver.find_element_by_css_selector('btn__content').click()

    # Shipping method
    continue_to_payment = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'btn__content')))
    continue_to_payment.click()

    # Payment method
    cc_number = wait.until(EC.presence_of_element_located((By.ID, 'number')))
    cc_number.send_keys(card_number)
    driver.find_element_by_id('name').send_keys(card_name)
    driver.find_element_by_id('expiry').send_keys(card_expiry)
    driver.find_element_by_id('verification_value').send_keys(card_ccv)
    driver.find_element_by_css_selector('btn__content').click()
except:
    driver.close()
    raise Exception
input()

exit()

# driver.get('https://ca.octobersveryown.com/collections/shop-all')


# s_len = len(driver.find_elements_by_css_selector('.search-bar .input-group-field'))
# driver.find_elements_by_css_selector('.search-bar .input-group-field')[s_len-1].send_keys('test')


search = wait.until(EC.visibility_of((By.CSS_SELECTOR, '.search-bar .input-group-field')))
print(search)
search[0].click()
search.send_keys('OG Hoodie')

input()
driver.close()


ok_size = driver.findElements(By.xpath("//button[text()='OK']")).size();

driver.findElements(By.xpath("//button[text()='OK']")).get(ok_size - 1).click();