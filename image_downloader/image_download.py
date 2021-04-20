import os
import json
import requests  # to sent GET requests
from bs4 import BeautifulSoup  # to parse HTML

# user can input a topic and a number
# download first n images from google image search

# The User-Agent request header contains a characteristic string
# that allows the network protocol peers to identify the application type,
# operating system, and software version of the requesting software user agent.
# needed for google search
usr_agent = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
}

SAVE_FOLDER = 'images'

def main():
    if not os.path.exists(SAVE_FOLDER):
        os.mkdir(SAVE_FOLDER)
    download_images()


def download_images():
    print('Start searching...')
    # request url, without usr_agent the permission gets denied

    counter = 0
    page = 1
    while counter < 300:

        MANGA = \
        'MANGA_URL/'+str("{:03d}".format(page))+'.jpg'

        response = requests.get(MANGA, headers=usr_agent)
        print('current page now:', page)
        print("{:03d}".format(page))
        print('url now:', MANGA)

        if response.status_code == 404:
            print('manga not found')
            exit(1)

        with open(str(page)+".jpg", 'wb') as file:
            file.write(response.content)
        print('Done')
        page += 1
        counter = counter + 1


if __name__ == '__main__':
    main()

# iterate url until 404, stop
