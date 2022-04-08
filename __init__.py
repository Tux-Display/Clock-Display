#Het includen/invoegen van benodigden libraries

from mycroft import MycroftSkill, intent_file_handler

##pip install nog?
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class ClockForSchoolDieWantIi(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    ##we moeten eig. bij elke lijn neer zetten wat het doen
    ##later handig voor presentaties

    #Het bestand van commands die klok laten zien
    @intent_file_handler('ii.want.die.school.for.clock.intent')

    #de functie die mycroft runt wanneer de gebruiker erom gevraagd heeft
    def handle_ii_want_die_school_for_clock(self, message):

        #Verteld de gebruiker na het activeren van clock command dat de klok op gaat starten
        self.speak_dialog('ii.want.die.school.for.clock')

        ##Eig. moet pi altijd in desktop env. opstarten
        ##en dan standaard klok

        #chrome browser voor de klok
        chrome_options = Options()
        chrome_options.add_argument("--kiosk")
        chrome_options.add_argument("--disable-application-cache")
        chrome_options.add_argument("disable-infobars")
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get("file:///opt/mycroft/skills/X-man-homescreen-css/index.html") ##point naar html klokje

#verteld aan mycroft de juiste function name voor deze skill
def create_skill():
    return ClockForSchoolDieWantIi()