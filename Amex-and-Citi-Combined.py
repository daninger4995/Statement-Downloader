import os
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

amex_username = "your_amex_username"
amex_password = "your_amex_password"
citi_username = "your_citi_username"
citi_password = "your_citi_password"
download_folder = "/path/to/download/folder"


def setup_webdriver(download_folder):
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": download_folder,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True,
    }
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=options)
    return driver


def login_amex(driver, username, password):
    driver.get("https://www.americanexpress.com/")
    driver.find_element_by_id("eliloUserID").send_keys(username)
    driver.find_element_by_id("eliloPassword").send_keys(password)
    driver.find_element_by_id("loginSubmit").click()


def login_citi(driver, username, password):
    driver.get("https://www.citi.com/credit-cards/home")
    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_id("signInBtn").click()

def download_and_rename_amex_statements(driver, download_folder):
WebDriverWait(driver, 10).until(
EC.presence_of_element_located((By.XPATH, '//*[@id="myca-menu"]/ul/li[3]/a'))
).click()

soup = BeautifulSoup(driver.page_source, "html.parser")
statement_links = soup.find_all("a", {"class": "your-statements-link"})

for link in statement_links:
    date = link["data-date"]
    last_four = link["data-last-four"]
    driver.get(link["href"])
    time.sleep(5)

    for file in os.listdir(download_folder):
        if file.endswith(".pdf"):
            os.rename(
                os.path.join(download_folder, file),
                os.path.join(download_folder, f"AMEX-{last_four}-Statement-{date}.pdf"),
            )

def download_and_rename_citi_statements(driver, download_folder):
WebDriverWait(driver, 10).until(
EC.presence_of_element_located((By.XPATH, '//a[contains(@href, "/account/statements")]'))
).click()