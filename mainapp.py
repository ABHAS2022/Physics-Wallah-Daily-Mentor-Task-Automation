import subprocess
from sub_main import main
from selenium import webdriver

cmd = '"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" --remote-debugging-port=8989 --user-data-dir="C:\\Users\\ABHAS\\Downloads\\chrome automation"'
print("Chrome Browser is opened")

# Start the Chrome process in the background
process = subprocess.Popen(cmd, shell=True)

# Continue with the rest of your code
main()

