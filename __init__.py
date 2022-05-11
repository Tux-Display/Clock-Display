#Het includen/invoegen van benodigden libraries

from calendar import c
from mycroft import MycroftSkill, intent_file_handler

## NOTES
## wat nou als we de driver variable blok stuk alles globaal maken, ergens in mycroft gedifned
## dan kunnen we, wanneer we een skill callen, de driver page veranderen (?)
## fking kut selenium


class ClockForSchoolDieWantIi(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    #Het bestand van commands die klok laten zien
    @intent_file_handler('ii.want.die.school.for.clock.intent')

    #de functie die mycroft runt wanneer de gebruiker erom gevraagd heeft
    def handle_ii_want_die_school_for_clock(self, message):

        #Verteld de gebruiker na het activeren van clock command dat de klok op gaat starten
        self.speak_dialog('ii.want.die.school.for.clock')

        with open('/opt/page.txt', 'w') as f:
            f.write('homescreen')
        
        

#verteld aan mycroft de juiste function name voor deze skill
def create_skill():
    return ClockForSchoolDieWantIi()