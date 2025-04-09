from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time

# Set up headless Chrome options
options = uc.ChromeOptions()
# options.add_argument('--headless=new')  # new mode is more stable as of Chrome 109+
# options.add_argument('--disable-gpu')
# options.add_argument('--no-sandbox')  # Good for Linux containers
# options.add_argument("--log-level=3")  # Fatal only
# options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.headless = True

# Path to your manually downloaded chromedriver
service = Service(executable_path=r"C:\Users\ubiqu\chrome_driver\chromedriver-win64\chromedriver.exe")

# Start the browser
# driver = webdriver.Chrome(service=service, options=options)
driver = uc.Chrome(options=options)

# Proceed with scraping
driver.get('https://www.indeed.com/jobs?q=sql+%24110%2C000&l=Buffalo%2C+NY&radius=25&salaryType=%24110%2C000&vjk=9fbacf82d2a0dc9b')

with open("page.html", "w", encoding="utf-8") as f:
    f.write(driver.page_source)

WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a.jcs-JobTitle'))
)

# time.sleep(5)

print(driver.page_source[:1000])  # Peek at the start of the HTML

job_titles = driver.find_elements(By.CLASS_NAME, 'jobTitle')
# class might be 'jcs-JobTitle'
company_names = driver.find_elements(By.CLASS_NAME, 'css-1h7lukg')
company_locations = driver.find_elements(By.CLASS_NAME, 'css-1restlb')
urls = driver.find_elements(By.XPATH, '//h2[starts-with(@class, "jobTitle")]/a')

for job_data in zip(job_titles, company_names, company_locations, urls):
    print('-------------------')
    job_name = job_data[0].text
    company_name = job_data[1].text
    location = job_data[2].text
    url = job_data[3].get_attribute('href')

    print(f"Job name: {job_name}")
    print(f"Company name: {company_name}")
    print(f"Location: {location}")
    print(f"URL: {url}")

driver.quit()