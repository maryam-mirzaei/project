from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
#import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
import json
from kala import kala


# number of item you want
item_requsted_cnt = 50

def webscrapping(search_item):
    datas =[]
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.maximize_window() # For maximizing window
    # driver.implicitly_wait(50)

    item=str(search_item).replace(' ','%20')
    driver.get(f'https://www.digikala.com/search/?q={item}')

    cart_a = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((
        By.CSS_SELECTOR, '.pos-relative.d-inline-flex.py-2.pr-2.pl-0.p-2-lg.bg-000.radius')))
    cart_a.send_keys(Keys.ESCAPE)
    #need for load complatly page after scroll end
    loop_numebr = 0
    scroll_count = 0 
    befor_product_len = 0
    # Get the height of the entire page
    screen_height = driver.execute_script("return window.screen.height;")
    
    while True: 
        product_list = driver.find_element(
            By.XPATH, '//*[@id="ProductListPagesWrapper"]/section/div[2]')
        time.sleep(2)
        products = product_list.find_elements(
            By.CSS_SELECTOR, '.product-list_ProductList__item__LiiNI')
        driver.execute_script('arguments[0].scrollIntoView(true);', products[-1])
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(products[-1]))
        if int(products[-1].get_attribute('data-product-index'))>= 50 or len(products) == befor_product_len :
            if (loop_numebr <= 2 and len(products) < item_requsted_cnt):
                loop_numebr += 1
            else:
                break    
        # Scroll to the element using JavaScript
        befor_product_len  = len(products)
 
    counter = 50 if len(products)>50 else len(products)

    #find elements
    divs=driver.find_elements(By.CSS_SELECTOR,'.product-list_ProductList__item__LiiNI')
    print('len divs:' + str(len(divs)))

    # changed dives to get 50 
    for div in divs[:counter]:
        # replaced with divs[:50]
        # if counter<=50: 
            a=div.find_element(By.TAG_NAME,'a')

            #link_data
            link_text = a.get_attribute('href')
            link_data = str(link_text)

            #img_data
            div1=a.find_element(By.CSS_SELECTOR,'.d-flex.ai-start.mx-auto')
            img=div1.find_element(By.TAG_NAME,'img')
            img_text = img.get_attribute('src')
            while img_text == None:
                img=div1.find_element(By.TAG_NAME,'img')
                img_text = img.get_attribute('src')
            img_data = str(img_text)

            #title_data   
            title_text = img.get_attribute('alt')
            title_data = str(title_text)

            #rate_data
            # div2=a.find_element(By.CSS_SELECTOR,'.mb-1.d-flex.ai-center.jc-between')
            rate_data = "-1"
            try:
                # if div2 != None:
                #     divs3=div2.find_elements(By.CSS_SELECTOR,'.d-flex.ai-center')
                #     w=True
                #     for div3 in divs3:
                #         if w:
                #             w=False
                #             continue
                #         else:
                #             p=div3.find_element(By.TAG_NAME,'p')
                #             rate_text = p.get_attribute('innerHTML')
                #             rate_data = str(rate_text)
                rate_data = div.find_element(
                By.CSS_SELECTOR, 'p.text-body2-strong.color-700').text
            except:
                pass

            #price_data
            price_data = '-1'
            try:
                price_data = div.find_element(
                    By.CSS_SELECTOR, '.d-flex.ai-center.jc-end.gap-1.color-700.color-400.text-h5.grow-1').text
                # print(f"price_data:{price_data}")
            except:
                pass
            d = {'link':link_data,'img':img_data,'title':title_data,'price':price_data,'rate':rate_data}
            # print(f"append item: {d['title']}")
            datas.append(d)
    print("json dumping")
    data = json.dumps(datas)

    with open('keyBoard1.json', mode='w',encoding='utf-8') as f:
        f.write(data)  
    print("end of webscraping")  
        