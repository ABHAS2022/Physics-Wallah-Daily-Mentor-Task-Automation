import subprocess
from sub_main import main
from selenium import webdriver
import os

os.makedirs("chrome automation")

cmd = '"chrome.exe" --remote-debugging-port=8989 --user-data-dir="chrome automation"'
print("Chrome Browser is opened")

# Start the Chrome process in the background
process = subprocess.Popen(cmd, shell=True)

# Continue with the rest of your code
main()

