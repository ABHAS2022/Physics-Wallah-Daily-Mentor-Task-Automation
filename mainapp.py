import subprocess
from sub_main import main
from selenium import webdriver
import os
from dotenv import load_dotenv


env_path = './paths_and_chats.env'
load_dotenv(dotenv_path=env_path)
CHROME_PATH = os.getenv('CHROME_PATH')
CHROME_AUTOMATION_FOLDER = os.getenv('CHROME_AUTOMATION')
if CHROME_AUTOMATION_FOLDER==None:
    os.makedirs("chrome automation")
    CHROME_AUTOMATION_FOLDER = 'chrome automation'
if CHROME_PATH==None:
    CHROME_PATH = 'chrome.exe'



cmd = f'"{CHROME_PATH}" --remote-debugging-port=8989 --user-data-dir="{CHROME_AUTOMATION_FOLDER}"'
print("Chrome Browser is opened")

# Start the Chrome process in the background
process = subprocess.Popen(cmd, shell=True)

# Continue with the rest of your code
main()

