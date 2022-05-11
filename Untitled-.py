#!/bin/python3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os

#chrome browser voor de klok
chrome_options = Options()
# Verwijderd infobars -> bar die liet weten dat het automated was
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches",["enable-automation"])
# chrome kios mode -> geen functies zodat de gebruiker niks kan doen
chrome_options.add_argument("--kiosk")
chrome_options.add_argument("--disable-application-cache")
chrome_options.add_argument("disable-infobars")
driver = webdriver.Chrome(chrome_options=chrome_options)
# open home pagina


while True:
    oude = ""
    # shutdowncheck = True
    driver.get("file:///opt/mycroft/skills/X-man-homescreen-css/homescreen.html")
    bestandsInhoud = open("/opt/page.txt", 'r').read()
    if bestandsInhoud == "homescreen" & oude != "homescreen":
        oude = "homescreen"
        driver.get("file:///opt/mycroft/skills/X-man-homescreen-css/homescreen.html")
    if bestandsInhoud == "clock" & oude != "clock":
        oude = "clock"
        driver.get("file:///opt/mycroft/skills/X-man-homescreen-css/clock.html")
    bestandsInhoud.close()