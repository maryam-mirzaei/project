def webscrapping(search_item):
    from selenium import webdriver
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    #import requests
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import time
    from selenium.webdriver.common.keys import Keys

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.maximize_window() # For maximizing window
    driver.implicitly_wait(20)

    item=str(search_item).replace(' ','%20')
    driver.get(f'https://www.digikala.com/search/?q={item}')
    time.sleep(10)

    cart_a = WebDriverWait(driver, 100).until(EC.visibility_of_element_located((
        By.CSS_SELECTOR, '.pos-relative.d-inline-flex.py-2.pr-2.pl-0.p-2-lg.bg-000.radius')))
    cart_a.send_keys(Keys.ESCAPE)

    time.sleep(5)
    driver.execute_script('window.scrollTo(0,3000)')
    time.sleep(60)

    img_data=''
    rate_data=''
    price_data=''
    title_data=''
    link_data=''

    counter = 0

    #find elements
    divs=driver.find_elements(By.CSS_SELECTOR,'.product-list_ProductList__item__LiiNI')
    print('len divs:' + str(len(divs)))

    for div in divs:
        if counter<=50:
            a=div.find_element(By.TAG_NAME,'a')

            #link_data
            link_text = a.get_attribute('href')
            link_data += str(link_text) + '\n'

            #img_data
            div1=a.find_element(By.CSS_SELECTOR,'.d-flex.ai-start.mx-auto')
            img=div1.find_element(By.TAG_NAME,'img')
            img_text = img.get_attribute('src')
            if img_text != None:
                img_data += str(img_text)+ '\n'

            #title_data   
            title_text = img.get_attribute('alt')
            title_data += str(title_text) + '\n'

            #rate_data
            div2=a.find_element(By.CSS_SELECTOR,'.mb-1.d-flex.ai-center.jc-between')
            divs3=div2.find_elements(By.CSS_SELECTOR,'.d-flex.ai-center')
            w=True
            for div3 in divs3:
                if w:
                    w=False
                    continue
                else:
                    p=div3.find_element(By.TAG_NAME,'p')
                    rate_text = p.get_attribute('innerHTML')
                    rate_data += str(rate_text) + '\n'

            #price_data
            div4=a.find_element(By.CSS_SELECTOR,'.d-flex.ai-center.jc-end.gap-1.color-700.color-400.text-h5.grow-1')
            span=div4.find_element(By.TAG_NAME,'span')
            price_text = span.get_attribute('innerHTML')
            price_data += str(price_text) + '\n'

        #set counter
            counter+=1

    # wirtting to files 
    with open(f'img.txt','w',encoding='utf-8') as handler:
        handler.write(img_data)
    with open(f'title.txt', 'w',encoding='utf-8') as handler:
        handler.write(title_data)
    with open(f'link.txt', 'w',encoding='utf-8') as handler:
        handler.write(link_data)
    with open(f'rate.txt', 'w',encoding='utf-8') as handler:
        handler.write(rate_data)
    with open(f'price.txt', 'w',encoding='utf-8') as handler:
        handler.write(price_data)

    #return count of product
    return(counter)
        
