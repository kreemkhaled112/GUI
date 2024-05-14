import requests , random , os , queue ,json , sys , webbrowser , logging  , sqlite3 , re , uuid , urllib3
from customtkinter import *
import undetected_chromedriver as uc
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from os.path import normpath, join
from selenium.webdriver.common.window import WindowTypes
import  urllib
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs
from pystyle import *
from threading import Thread , Lock
from time import sleep ,time
from pystyle import *
from configparser import ConfigParser
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt , pyqtSignal , QThread
from datetime import datetime
import concurrent.futures
urllib3.disable_warnings()

conn = sqlite3.connect('pages_functions\info.db', check_same_thread=False)
cursor = conn.cursor()
config = ConfigParser()
config.read('pages_functions\settings.ini')
def Header():
    headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7',
    'dpr': '1',
    'priority': 'u=0, i',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-full-version-list': '"Chromium";v="124.0.6367.119", "Google Chrome";v="124.0.6367.119", "Not-A.Brand";v="99.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
}
    return headers
def Header_www():
    headers  = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en,en-US;q=0.9,ar;q=0.8,ar-EG;q=0.7',
    'cache-control': 'max-age=0',
    'dpr': '1',
    'priority': 'u=0, i',
    'referer': 'https://www.facebook.com/',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-full-version-list': '"Chromium";v="124.0.6367.119", "Google Chrome";v="124.0.6367.119", "Not-A.Brand";v="99.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
}
    return headers
def cookie_format(cookie):
    cookie_pairs = cookie.split(';')
    cookie = {}
    for pair in cookie_pairs:
        if '=' in pair:
            key, value = pair.split('=', 1)
            cookie[key] = value
    return cookie

class QMessage(CTk):
    def __init__(self, text , title = None , *args, **kwargs) :
        super().__init__(*args, **kwargs)
        self.title('Follow')
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - 200) // 2
        y = (screen_height - 100) // 2
        self.geometry(f"200x100+{x}+{y}")
        self.resizable(False,False)
        self.title(title)
        CTkLabel(self,text=text ).place(x=25,y=15)
        self.value = StringVar()
        ok = CTkButton(self, text="Ok", width=100, command=self.Ok)
        ok.place(x=45, y=55)

    def Ok(self):
        self.value.set("Ok")
        self.destroy()