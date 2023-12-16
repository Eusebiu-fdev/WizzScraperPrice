import os
import time
from datetime import datetime
from openpyxl import load_workbook
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
import random
import pandas as pd

# Headers
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
]

options = uc.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument('--disable-gpu')
options.add_argument('--enable-js')

driver = uc.Chrome(options=options)

# XLS file path
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
xls_file_path = os.path.join(desktop_path, "price_data.xlsx")

time.sleep(3)

try:
    # Checks if the XLS file exists; if not, create it with headers and columns
    is_file_exist = os.path.exists(xls_file_path)
    if not is_file_exist:
        data = {
        "Date": [],
        "Price": [],
        "Time": []
        }

    df = pd.DataFrame(data)
    df.to_excel(xls_file_path, index=False)

    while True:
        chosen_user_agent = random.choice(user_agents)
        options.add_argument(f'user-agent={chosen_user_agent}')

        wizz_air_url = 'https://wizzair.com/ro-ro#/booking/select-flight/ZAZ/OTP/2023-12-26/null/1/0/0/null'

        driver.get(wizz_air_url)

        price_element = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/main/div/div/div[1]/div[3]/div[1]/div[4]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div/div/div/div'))
        )

        price_value = price_element.text.strip()
        current_date = datetime.now().strftime("%d/%m/%y")
        current_time = datetime.now().strftime("%H:%M:%S")

        wb = load_workbook(xls_file_path)
        sheet = wb.active
        new_row = [current_date, price_value, current_time]
        sheet.append(new_row)
        wb.save(xls_file_path)
        wb.close()

        time.sleep(300)

except Exception as e:
    print(f"Error occurred: {str(e)}")

finally:
    if 'driver' in locals():
        driver.quit()
