from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
def amazon(product_name):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://www.amazon.in/')

    wait = WebDriverWait(driver, 10)
    search_box = wait.until(EC.presence_of_element_located((By.ID, 'twotabsearchtextbox')))
    search_box.send_keys(product_name)
    search_box.send_keys(Keys.RETURN)

    # Wait for product results to load
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 's-main-slot')))

    # Fetch product details (names and prices)
    product_details = driver.find_elements(By.CLASS_NAME, 'a-size-medium')
    product_prices = driver.find_elements(By.CLASS_NAME, 'a-price-whole')
    product_images = driver.find_elements(By.CLASS_NAME, 's-image')

    # Debugging prints to check if elements are found
    print(f"Amazon Found {len(product_details)} products")
    print(f"Found {len(product_prices)} prices")
    print(f"Found {len(product_images)} images")
    # if product_details:
    #     for details in product_details:
    #         if len(details) == 3:
    #             name, price, img_url = details
    #             # process the name, price, and img_url
    #         else:
    #             print(f"Unexpected data format: {details}")
    # else:
    #     print("No data received from amazon_details.")


    products = []
    for i in range(min(len(product_details), len(product_images))):
        try:
            name = product_details[i].text
            price = product_prices[i].text if i < len(product_prices) else 'Price not available'
            img_url = product_images[i].get_attribute('src')
            products.append((name, price, img_url))
        except Exception as e:
            print(f"Error scraping product {i}: {e}")

    driver.quit()
    return products

def flipkart(product_name):
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    # Disable headless for debugging
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://www.flipkart.com/')

    wait = WebDriverWait(driver, 10)

    # Close the login popup if it appears
    try:
        close_login_popup = wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='✕']")))
        close_login_popup.click()
    except Exception as e:
        print("No login popup found or failed to close it.")

    # Search for the product
    search_box = wait.until(EC.presence_of_element_located((By.NAME, 'q')))
    search_box.send_keys(product_name)
    search_box.send_keys(Keys.RETURN)

    # Wait for the product results to load
    # time.sleep(5)  # Wait for page to load completely

    # Take a screenshot to verify that the search page has loaded
    # driver.save_screenshot("flipkart_search.png")

    # Locate the product details (use correct XPaths after inspecting the page)
    try:
        # Adjusted XPaths for product names, prices, and images
        product_details = driver.find_elements(By.XPATH, '//div[contains(@class, "col-7-12")]')  # Adjust this
        product_prices = driver.find_elements(By.XPATH, '//div[contains(@class, "hl05eU")]')   # Adjust this
        product_images = driver.find_elements(By.XPATH, '//img[contains(@class, "DByuf4")]')   # Adjust this

        # Debugging prints to check if elements are found
        print(f"Flipkart Found {len(product_details)} products")
        print(f"Found {len(product_prices)} prices")
        print(f"Found {len(product_images)} images")

        products = []
        for i in range(min(len(product_details), len(product_images))):
            try:
                name = product_details[i].text
                price = product_prices[i].text if i < len(product_prices) else 'Price not available'
                img_url = product_images[i].get_attribute('src')
                products.append((name, price, img_url))
            except Exception as e:
                print(f"Error scraping product {i}: {e}")
    except Exception as e:
        print(f"Error finding products: {e}")

    driver.quit()
    return products