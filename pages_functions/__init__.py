from customtkinter import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
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
# import pygame
import logging
from configparser import ConfigParser
import PyQt5.sip
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import ctypes


awareness = ctypes.c_int()
ctypes.windll.shcore.GetProcessDpiAwareness(0, ctypes.byref(awareness))

conn = sqlite3.connect('pages_functions\info.db', check_same_thread=False)
cursor = conn.cursor()
def Header():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/115.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
    }
    return headers

