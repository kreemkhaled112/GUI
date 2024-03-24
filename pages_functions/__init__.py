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
import  os, json, re 
from os.path import normpath, join
import random 
import pyautogui as pg
import pyperclip as py
from selenium.webdriver.common.window import WindowTypes
import  urllib
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs
import requests , random , os , queue ,json , sys
from pystyle import *
from threading import Thread
from time import sleep ,time
import re
import sqlite3
from pystyle import *
import pygame
import logging
from configparser import ConfigParser
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt , pyqtSignal , QThread
from datetime import datetime
import webbrowser

conn = sqlite3.connect('pages_functions\info.db', check_same_thread=False)
cursor = conn.cursor()
def Header():
    headers = {
        'authority': 'mbasic.facebook.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en,en-US;q=0.9,ar;q=0.8,ar-EG;q=0.7',
        'cache-control': 'max-age=0',
        'sec-ch-prefers-color-scheme': 'dark',
        'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        'sec-ch-ua-full-version-list': '"Not A(Brand";v="99.0.0.0", "Google Chrome";v="121.0.6167.140", "Chromium";v="121.0.6167.140"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    }
    return headers

def Update_cookies(old_cookie, new_cookie):
    try: cursor.execute(f"UPDATE account SET cookies = '{new_cookie}' WHERE cookies = '{old_cookie}'");conn.commit()
    except: 
        print("Faild Update")
        return "Faild Update"
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
class CustomMessageBox(QDialog):
    def init(self, message, parent=None):
        super(CustomMessageBox, self).init(parent)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setGeometry(300, 200, 600, 200)
        self.setStyleSheet("border-radius: 15px; border:1px solid #6422ba; background-color: #1f2224;")

        layout = QVBoxLayout()
        label = QLabel(message)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("border: none;color:white")
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        label.setFont(font)
        layout.addWidget(label)

        button = QPushButton("OK")
        button.setCursor(QCursor(Qt.PointingHandCursor))
        button.setMinimumHeight(50)
        button.setStyleSheet("""
        QPushButton{
        border:none;
        background-color:#6422ba;
        border-radius:15px;
        color:white
        }
        QPushButton:hover{
        background-color: #5e1fb0;
        }
        QPushButton:pressed{
        background-color: #6c24ca;
        }
""")
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        button.setFont(font)
        button.clicked.connect(self.accept)
        layout.addWidget(button)

        self.setLayout(layout)


