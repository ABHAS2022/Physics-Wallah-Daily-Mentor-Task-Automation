import os
import random
from utils import perform_operation


def main():
    """
    Main function to execute the script.
    """
    print("Starting script...")

    list_of_webaddress_of_chats = [
    #     Open the mentorship chats and then copy paste their addresses here in the list and separate the different addresses by the comma    
        #     ]
    files_path = YOUR_FOLDER_PATH_WHERE_QUESTIONS_ARE_KEPT
    files = [os.path.join(files_path, i) for i in os.listdir(files_path)]

    for url in list_of_webaddress_of_chats:
        perform_operation(url, random.sample(files,len(files)))

    print("Script finished.")

