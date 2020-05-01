# -*- coding: utf-8 -*-
"""
Created on Sun Apr 20 23:46:07 2020

@author: Sachin Sharma
"""

import time
import os
from os.path import expanduser

from win10toast import ToastNotifier
notify = ToastNotifier()

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from webdriver_manager.chrome import ChromeDriverManager

from whatsapp import send_whatsapp



def show_notification(msg_class):
    if msg_class == "LOGIN":
        title = "Redirecting to BigBasket Website"
        message = "Please login to you BigBasket account"
        
    if msg_class == "START":
        title = "Monitoring has started"
        message = "You can minimize the window if you want. You will receive a notification if a slot is found"
        send_whatsapp(title + " : " + message)
        
    if msg_class == "SUCCESS":
        title = "Slot found!!"
        message = "Please check the BigBasket app/website"
        send_whatsapp(title + " : " + message)
        
    if msg_class == "EMPTY_BASKET":
        title = "Empty Basket!"
        message =  "You might want to pre-load your basket. It will save time during checkout."
    
    
    if msg_class == "LOGIN_ERROR":
        title = "Error"
        message = "There was some error during login. Please restart the program"
    
    
    if msg_class == "BAD_CONNECTION":
        title = "Bad Internet Connection"
        message = "There was some error connecting to the website. If it continues, restart the program."
    
    
    print(title + " : " + message)
    notify.show_toast(title,message,threaded=True)


def is_driver_installed():
    found = None
    driver_dir = expanduser('~') + "//" + ".wdm"
    
    for path in os.walk(driver_dir):
        if "chromedriver.exe" in path[2]:
            found = path[0] + "//" + "chromedriver.exe"
            break
        
    return found
    
def start_driver(url, login):
    
    driver_path = is_driver_installed()
    
    if not driver_path:
        driver = webdriver.Chrome(ChromeDriverManager().install())    
    else:
        driver = webdriver.Chrome(driver_path)
    
    driver.maximize_window()
    
    show_notification("LOGIN")   
        
    driver.get(url+login)
    
    try:
        WebDriverWait(driver, 100).until(
            lambda x : driver.current_url == url)
    except:
        show_notification("LOGIN_ERROR")
        return False       
    
    return driver

def get_slots(url, login, basket):
    driver = start_driver(url, login)    
    
    if driver:
        show_notification("START")
    
    
    while driver:  
        driver.get(url+basket)
        time.sleep(5)
        try:
            driver.find_element_by_xpath("//button[@id = 'checkout']").click()
            
        except:
            try:
                driver.find_element_by_id('top_header_with_band')
                show_notification("EMPTY_BASKET")
            except:
                show_notification("BAD_CONNECTION")
        
        
        if "checkout" in driver.current_url:
            show_notification("SUCCESS")
            time.sleep(20)
        
        time.sleep(15)
    
def main():
    url = "https://www.bigbasket.com/"
    login = "auth/login"
    basket = "basket?ver=1"
    get_slots(url, login, basket)
    
 
if __name__ == "__main__":
    main()