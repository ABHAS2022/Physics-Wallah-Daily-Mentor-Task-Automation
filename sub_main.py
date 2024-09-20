import os
import sys
import json
import random
from dotenv import load_dotenv
from utils import perform_operation, get_daily_quote


def main():
    """
    Main function to execute the script.
    """

    env_path = './paths_and_chats.env'
    load_dotenv(dotenv_path=env_path)
    print("Starting script...")
    # Get the JSON string from command-line arguments
    data = ""
    with open('chat_list.json', 'r') as file:
        data = json.load(file)
    LIST_OF_CHATS = data['LIST_OF_CHATS']


    list_of_webaddress_of_chats = LIST_OF_CHATS
    # print(list_of_webaddress_of_chats)

    question_files_path = os.getenv('PATH_FOR_DAILY_QUESTION_PICTURES')
    daily_pdf_path = os.getenv('PATH_FOR_DAILY_PDF_FOLDER')

    pdfs = [os.path.join(daily_pdf_path,i) for i in os.listdir(daily_pdf_path)]
    files = [os.path.join(question_files_path, i) for i in os.listdir(question_files_path)]
    pdfs = random.sample(pdfs,len(pdfs))
    files = random.sample(files,len(files))
    quote, author = get_daily_quote()
    string_to_sent = quote + '\n' + author
    for url in list_of_webaddress_of_chats:
        perform_operation(url, files,pdfs[0],quote = string_to_sent)

    print("Script finished.")

