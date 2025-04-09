import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time

options = uc.ChromeOptions()
options.headless = True
driver = uc.Chrome(options=options)

driver.get("https://www.indeed.com/jobs?q=sql+%24110%2C000&l=Buffalo%2C+NY&radius=25")

time.sleep(5)

job_titles = driver.find_elements(By.CSS_SELECTOR, 'a[data-jk]')
print(f"{len(job_titles)} job titles found")

for job in job_titles:
    print(job.text)
    print(job.get_attribute("href"))
