import requests
from bs4 import BeautifulSoup
import random
from  threading import *
import os
import time
from os import path
from Cookies import selected_cookies
from gui import Ui_MainWindow

class AutoReact:
    def __init__(self,ui:Ui_MainWindow):
        self.ui = ui
        self.is_paused = False

        self.headers = {
            'authority': 'mbasic.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
            'cache-control': 'max-age=0',
            'dpr': '1.25',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Microsoft Edge";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
            'sec-ch-ua-full-version-list': '"Microsoft Edge";v="117.0.2045.47", "Not;A=Brand";v="8.0.0.0", "Chromium";v="117.0.5938.132"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"15.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.47',
            'viewport-width': '659',
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)
        self.ui.react_btn.clicked.connect(lambda : Thread(target=self.auto_react).start())
        self.ui.react_stop_btn.clicked.connect(lambda : Thread(target=self.auto_react).start())


    def auto_react(self):
        if self.is_paused == False :
            self.is_paused == True
        elif self.is_paused == True :
            self.is_paused == False

        if not selected_cookies:
            self.ui.react_status.setText('Please login and select accounts')
            return
        post_link = self.ui.react_link_input.text().replace('www','mbasic')
        if not post_link:
            self.ui.react_status.setText('Please add post link!')
            return
        while self.is_paused :
            for i, (account_name, cookies) in enumerate(selected_cookies, start=1):
                self.ui.react_status.setText('Starting...')
                if isinstance(cookies, list):
                    cookies = {cookie['name']: cookie['value'] for cookie in cookies}

                if self.ui.like.isChecked():
                    reaction_type = 1
                elif self.ui.love.isChecked():
                    reaction_type = 2
                elif self.ui.care.isChecked():
                    reaction_type = 16
                elif self.ui.haha.isChecked():
                    reaction_type = 4
                elif self.ui.wow.isChecked():
                    reaction_type = 3
                elif self.ui.sad.isChecked():
                    reaction_type = 7
                elif self.ui.angry.isChecked():
                    reaction_type = 8
                elif self.ui.random.isChecked():
                    reaction_type = random.choice([1, 2, 3, 16, 4, 8, 7])

                response = self.session.get(post_link, cookies=cookies, headers=self.headers)
                soup = BeautifulSoup(response.text, 'html5lib')
                if response.status_code == 200:
                    # Check if post_link contains "comment_id"
                    if "comment_id" in post_link:
                        # If yes, get the second href
                        comment_id = post_link.split('comment_id=')[1]
                        target_element = soup.find('div', {'id': {comment_id}})
                        url = target_element.find('a', href=lambda href: href and href.startswith('/reactions/picker/'))['href']
                    else:
                        # If not, get the first href
                        url = next((a['href'] for a in soup.find_all('a', href=True) if a['href'].startswith("/reactions/picker/")), None)
                    if not url:
                        self.ui.react_status.setText(f'Reaction with account "{account_name}" is failed! Skipping...')
                        continue
                    response = self.session.get(f'https://mbasic.facebook.com{url}', cookies=cookies, headers=self.headers)
                    if response.status_code == 200:
                        soup = BeautifulSoup(response.text, 'html5lib')
                        url_2 = soup.find('a', href=lambda href: href and f'reaction_type={reaction_type}' in href)['href']
                        response = self.session.get(f'https://mbasic.facebook.com{url_2}', cookies=cookies, headers=self.headers)
                        if response.status_code ==200:
                            self.ui.react_status.setText(f'Reacted With account "{account_name}"... {i} of {len(selected_cookies)}')
                        else:
                            self.ui.react_status.setText(f'Reaction with account "{account_name}" is failed! Skipping...')

                time.sleep(int(self.ui.react_slider.value()))
            self.ui.react_status.setText(f'Finished.')
            break
