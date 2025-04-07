from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

def amazon(product_name):
    chrome_options = Options()
    chrome_options.add_argument("--headless") 
    chrome_options.add_argument("--disable-gpu") 

    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://www.amazon.in/events/greatfreedomsale/?_encoding=UTF8&ref_=IN_Prime_ACQ_GW_Hero_Aug_ART24_T2_Desktop_KSD&pd_rd_w=LGAXT&content-id=amzn1.sym.19032bda-20e9-4dcd-bc7c-d688a04abf7e&pf_rd_p=19032bda-20e9-4dcd-bc7c-d688a04abf7e&pf_rd_r=4D5B65D146HMEXYDN1BM&pd_rd_wg=XTSic&pd_rd_r=2ab7936f-d984-44bb-9c1a-5ba580f9261b')

    wait = WebDriverWait(driver, 10)

    div_class_name='nav-search-field'

    wait=WebDriverWait(driver,10)

    div_element=wait.until(EC.presence_of_element_located((By.CLASS_NAME,div_class_name)))

    search_box=div_element.find_element(By.XPATH, './/input[@type="text"]')

    search_box.send_keys(product_name)
    search_box.send_keys(Keys.RETURN)  # enter

    div2_class_name='puisg-col-inner'

    # wait.until(EC.presence_of_element_located((By.CLASS_NAME, div2_class_name)))
    
    product_details=driver.find_elements(By.CLASS_NAME,div2_class_name)
    l=[]

    for i in product_details:
        l.append(i.text)
    
    
    driver.quit()


    return l
    
    

def flipkart(product_name):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://www.flipkart.com/')

    div_class_name='_2SmNnR'

    wait=WebDriverWait(driver,10)

    div_element=wait.until(EC.presence_of_element_located((By.CLASS_NAME,div_class_name)))

    search_box=div_element.find_element(By.XPATH, './/input[@type="text"]')

    search_box.send_keys(product_name)
    search_box.send_keys(Keys.RETURN)  # enter

    div2_class_name='yKfJKb'

    product_details=driver.find_elements(By.CLASS_NAME,div2_class_name)
    l=[]

    for i in product_details:
        l.append(i.text)

    driver.quit()
        
    return l

if __name__=="__main__":
    product_name = input("Enter product name: ")
    amazon_details = amazon(product_name)
    flipkart_details = flipkart(product_name)
    print("Amazon Results:", amazon_details)
    print("Flipkart Results:", flipkart_details)
