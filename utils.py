import time
import requests
import os
from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


env_path = './paths_and_chats.env'
load_dotenv(dotenv_path=env_path)
NUMBER_OF_QUESTIONS = int(os.getenv('NUMBER_OF_DAILY_QUESTIONS_TO_SEND'))
TEXT_TO_BE_SENT_WITH_PDF = os.getenv('MESSAGE_TO_BE_SENT_ALONG_WITH_DAILY_PDF')


def daily_questions(driver, filenames):
    """
    Function to upload files and create polls in the web application.

    Args:
        driver (webdriver.Chrome): The Selenium WebDriver instance.
        filenames (list): List of file paths to be uploaded.
    """

    for filename in filenames[:NUMBER_OF_QUESTIONS]:
            print(f"Processing file: {filename}")

        # try:
            # Upload the file
            print("Waiting for file input element to be visible...")
            file_input = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[2]/div/div/div[2]/div[2]/input'))
            )
            print("Uploading file...")
            file_input.send_keys(filename)

            # WebDriverWait(driver,3)
            # Submit the file
            time.sleep(4)
            print("Waiting for submit button to be clickable...")
            submit_button = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]'))
            )
            print("Clicking submit button...")
            submit_button.click()
            time.sleep(3)

            # Create a poll
            print("Waiting for create poll button to be clickable...")
            create_poll_button = WebDriverWait(driver, 120).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[2]/div/div/div[1]'))
            )
            print("Clicking create poll button...")
            create_poll_button.click()

            # Fill in poll information
            print("Filling in poll information...")
            poll_title = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located(
                    (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/input'))
            )
            poll_title.send_keys("Tick the correct Options")

            options = [
                [(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]/input'),"1"],
                [(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div[2]/div[3]/input'), "2"],
                [(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div[2]/div[4]/input'), "3"],
                [(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div[2]/div[5]/input'), "4"]
            ]

            for xpath, value in options:
                option = WebDriverWait(driver, 120).until(
                    EC.presence_of_element_located(xpath)
                )
                option.send_keys(value)

            submit_poll = WebDriverWait(driver, 120).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div[4]/button/span/span'))
            )
            submit_poll.click()
            print("Poll created successfully.")

            time.sleep(3)  # Optional, just to ensure any post-submit actions are completed


def switchiframe(driver):
    print("Waiting for iframe to be available and switching to it...")
    wait = WebDriverWait(driver, 10)
    iframe = wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "mentorshipIframe")))


def daily_pdf(driver,filename):
    try:
        # switchiframe(driver)
        print(f"Writing the text {TEXT_TO_BE_SENT_WITH_PDF}")
        # /html/body/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/input
        text_input = WebDriverWait(driver,120).until(
            EC.presence_of_element_located((
                By.XPATH,'/html/body/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/input')
            )
        )
        text_input.send_keys(TEXT_TO_BE_SENT_WITH_PDF)
        print("Waiting for submit button to be clickable...")
        submit_button = WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]'))
        )
        print("Clicking submit button...")
        submit_button.click()
        time.sleep(3) 



        print("Waiting for file input element to be visible...")
        file_input = WebDriverWait(driver, 120).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[2]/div/div/div[2]/div[2]/input'))
        )
        print("Uploading file...")
        file_input.send_keys(filename)
        print("Waiting for submit button to be clickable...")
        time.sleep(4)
        submit_button = WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]'))
        )
        print("Clicking submit button...")
        submit_button.click()
        time.sleep(3) 
    except:
        driver.refresh()
        # switchiframe(driver)
        daily_pdf(driver, filename) 

def get_daily_quote():
    x = requests.get("https://zenquotes.io/api/today")
    dict = x.json()[0]
    quote = dict['q']
    author = dict['a']
    return quote, author

def sending_quotes(website, driver,quote):
    text_input = WebDriverWait(driver,120).until(
    EC.presence_of_element_located((
            By.XPATH,'/html/body/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/input')
        )
    )
    text_input.send_keys("Here is a daily quote for motivation")
    time.sleep(2)
    print("Waiting for submit button to be clickable...")
    submit_button = WebDriverWait(driver, 120).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]'))
    )
    print("Clicking submit button...")
    submit_button.click()
    time.sleep(2)
    text_input = WebDriverWait(driver,120).until(
    EC.presence_of_element_located((
            By.XPATH,'/html/body/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/input')
        )
    )
    text_input.send_keys(quote)
    time.sleep(2)
    print("Waiting for submit button to be clickable...")
    submit_button = WebDriverWait(driver, 120).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]'))
    )
    print("Clicking submit button...")
    submit_button.click()
    time.sleep(2)

def perform_operation(website, files, pdf_path, quote):
    """
    Function to open a website, switch to an iframe, and perform daily tasks.

    Args:
        website (str): The URL of the website to open.
        files (list): List of file paths to be uploaded.
    """
    print(f"Opening website: {website}")

    opt = Options()
    opt.add_experimental_option("debuggerAddress", "localhost:8989")
    driver = webdriver.Chrome(options=opt)
    driver.get(website)
    try:
        switchiframe(driver)
    except:
        driver.get(website)
        switchiframe(driver)

    print("Sending DailY Inspirational Quote")
    sending_quotes(website=website,driver=driver,quote=quote)

    print("Sending Daily pdfs")
    daily_pdf(driver=driver,filename=pdf_path)

    print("Performing daily tasks...")
    daily_questions(driver, files)

    print("Operation completed.")
    driver.quit()
