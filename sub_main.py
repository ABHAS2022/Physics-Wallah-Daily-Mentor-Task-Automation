import os
import random
from utils import perform_operation, get_daily_quote


def main():
    """
    Main function to execute the script.
    """
    print("Starting script...")

    list_of_webaddress_of_chats = [
        'https://www.pw.live/study/batches/lakshya-jee-2025-095106/batch-overview/mentor-ship/%257B%2522_id%2522%253A%252265d862392b1da90018ad8f3b%2522%252C%2522name%2522%253A%2522Lakshya%2520JEE%25202025%2522%252C%2522conversationId%2522%253A%2522661f6d309d4791f44def1fb8%2522%252C%2522groupId%2522%253A%2522661f6d272a2f23567f2e7da9%2522%257D',
        'https://www.pw.live/study/batches/lakshya-jee-2025-095106/batch-overview/mentor-ship/%257B%2522_id%2522%253A%252265d862392b1da90018ad8f3b%2522%252C%2522name%2522%253A%2522Lakshya%2520JEE%25202025%2522%252C%2522conversationId%2522%253A%2522661f6d309d4791f44def1fbb%2522%252C%2522groupId%2522%253A%2522661f6d282a2f23567f2e7dfe%2522%257D',
        'https://www.pw.live/study/batches/lakshya-jee-2025-095106/batch-overview/mentor-ship/%257B%2522_id%2522%253A%252265d862392b1da90018ad8f3b%2522%252C%2522name%2522%253A%2522Lakshya%2520JEE%25202025%2522%252C%2522conversationId%2522%253A%2522661f6d309d4791f44def1fbe%2522%252C%2522groupId%2522%253A%2522661f6d282a2f23567f2e7e53%2522%257D',
        'https://www.pw.live/study/batches/lakshya-jee-2025-095106/batch-overview/mentor-ship/%257B%2522_id%2522%253A%252265d862392b1da90018ad8f3b%2522%252C%2522name%2522%253A%2522Lakshya%2520JEE%25202025%2522%252C%2522conversationId%2522%253A%2522661f6d319d4791f44def1fc1%2522%252C%2522groupId%2522%253A%2522661f6d282a2f23567f2e7ea6%2522%257D',
        'https://www.pw.live/study/batches/lakshya-jee-2025-095106/batch-overview/mentor-ship/%257B%2522_id%2522%253A%252265d862392b1da90018ad8f3b%2522%252C%2522name%2522%253A%2522Lakshya%2520JEE%25202025%2522%252C%2522conversationId%2522%253A%2522661f6d319d4791f44def1fc4%2522%252C%2522groupId%2522%253A%2522661f6d282a2f23567f2e7efa%2522%257D',
        'https://www.pw.live/study/batches/lakshya-jee-2025-095106/batch-overview/mentor-ship/%257B%2522_id%2522%253A%252265d862392b1da90018ad8f3b%2522%252C%2522name%2522%253A%2522Lakshya%2520JEE%25202025%2522%252C%2522conversationId%2522%253A%2522661f6d92beaa6aaa731d2798%2522%252C%2522groupId%2522%253A%2522661f6d892a2f23567f2fa0ea%2522%257D',
        'https://www.pw.live/study/batches/lakshya-jee-2025-095106/batch-overview/mentor-ship/%257B%2522_id%2522%253A%252265d862392b1da90018ad8f3b%2522%252C%2522name%2522%253A%2522Lakshya%2520JEE%25202025%2522%252C%2522conversationId%2522%253A%2522661f6d92beaa6aaa731d279b%2522%252C%2522groupId%2522%253A%2522661f6d892a2f23567f2fa13f%2522%257D'
    ]

    files_path = 'C:\\Users\\ABHAS\\Downloads\\Maybe Some Idea\\Physics Wallah Automation\\question files'
    pdf_path = 'C:\\Users\\ABHAS\Downloads\\Maybe Some Idea\\Physics Wallah Automation\\pdf_file'
    pdfs = [os.path.join(pdf_path,i) for i in os.listdir(pdf_path)]
    files = [os.path.join(files_path, i) for i in os.listdir(files_path)]
    pdfs = random.sample(pdfs,len(pdfs))
    files = random.sample(files,len(files))
    quote, author = get_daily_quote()
    string_to_sent = quote + '\n' + author
    for url in list_of_webaddress_of_chats:
        perform_operation(url, files,pdfs[0],quote = string_to_sent)

    print("Script finished.")

