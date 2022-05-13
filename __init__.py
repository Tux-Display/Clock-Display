#Het includen/invoegen van benodigden libraries

# from calendar import c
import os
from mycroft import MycroftSkill, intent_file_handler


class ClockForSchoolDieWantIi(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        

    #Het bestand van commands die klok laten zien
    @intent_file_handler('ii.want.die.school.for.clock.intent')

    #de functie die mycroft runt wanneer de gebruiker erom gevraagd heeft
    def handle_ii_want_die_school_for_clock(self, message):
        print(os.system("cat /proc/self/environ >> /tmp/test.txt"))

        #Verteld de gebruiker na het activeren van clock command dat de klok op gaat starten
        self.speak_dialog('ii.want.die.school.for.clock')

        with open('/opt/page.txt', 'w') as f:
            f.write('homescreen')
        
        

#verteld aan mycroft de juiste function name voor deze skill
def create_skill():
    
    # maakt listener aan die checkt wanneer het bestand voor de homescreen change veranderd
    
    os.system('mkdir /tmp/.homescreenskilldata/ 2>/dev/null')
    os.system('rm /tmp/.homescreenskilldata/fileChecker.py 2>/dev/null')
    os.system('touch /tmp/.homescreenskilldata/fileChecker.py')
    os.system('echo "IyEvYmluL3B5dGhvbjMKZnJvbSBzZWxlbml1bSBpbXBvcnQgd2ViZHJpdmVyCmZyb20gc2VsZW5pdW0ud2ViZHJpdmVyLmNocm9tZS5vcHRpb25zIGltcG9ydCBPcHRpb25zCmZyb20gd2ViZHJpdmVyX21hbmFnZXIuY2hyb21lIGltcG9ydCBDaHJvbWVEcml2ZXJNYW5hZ2VyCmltcG9ydCBvcwoKI2Nocm9tZSBicm93c2VyIHZvb3IgZGUga2xvawpjaHJvbWVfb3B0aW9ucyA9IE9wdGlvbnMoKQojIFZlcndpamRlcmQgaW5mb2JhcnMgLT4gYmFyIGRpZSBsaWV0IHdldGVuIGRhdCBoZXQgYXV0b21hdGVkIHdhcwpjaHJvbWVfb3B0aW9ucy5hZGRfZXhwZXJpbWVudGFsX29wdGlvbigidXNlQXV0b21hdGlvbkV4dGVuc2lvbiIsIEZhbHNlKQpjaHJvbWVfb3B0aW9ucy5hZGRfZXhwZXJpbWVudGFsX29wdGlvbigiZXhjbHVkZVN3aXRjaGVzIixbImVuYWJsZS1hdXRvbWF0aW9uIl0pCiMgY2hyb21lIGtpb3MgbW9kZSAtPiBnZWVuIGZ1bmN0aWVzIHpvZGF0IGRlIGdlYnJ1aWtlciBuaWtzIGthbiBkb2VuCmNocm9tZV9vcHRpb25zLmFkZF9hcmd1bWVudCgiLS1raW9zayIpCmNocm9tZV9vcHRpb25zLmFkZF9hcmd1bWVudCgiLS1kaXNhYmxlLWFwcGxpY2F0aW9uLWNhY2hlIikKY2hyb21lX29wdGlvbnMuYWRkX2FyZ3VtZW50KCJkaXNhYmxlLWluZm9iYXJzIikKZHJpdmVyID0gd2ViZHJpdmVyLkNocm9tZShjaHJvbWVfb3B0aW9ucz1jaHJvbWVfb3B0aW9ucykKIyBvcGVuIGhvbWUgcGFnaW5hCgoKd2hpbGUgVHJ1ZToKICAgIG91ZGUgPSAiIgogICAgIyBzaHV0ZG93bmNoZWNrID0gVHJ1ZQogICAgZHJpdmVyLmdldCgiZmlsZTovLy9vcHQvbXljcm9mdC9za2lsbHMvWC1tYW4taG9tZXNjcmVlbi1jc3MvaG9tZXNjcmVlbi5odG1sIikKICAgIGJlc3RhbmRzSW5ob3VkID0gb3BlbigiL29wdC9wYWdlLnR4dCIsICdyJykucmVhZCgpCiAgICBpZiBiZXN0YW5kc0luaG91ZCA9PSAiaG9tZXNjcmVlbiIgJiBvdWRlICE9ICJob21lc2NyZWVuIjoKICAgICAgICBvdWRlID0gImhvbWVzY3JlZW4iCiAgICAgICAgZHJpdmVyLmdldCgiZmlsZTovLy9vcHQvbXljcm9mdC9za2lsbHMvWC1tYW4taG9tZXNjcmVlbi1jc3MvaG9tZXNjcmVlbi5odG1sIikKICAgIGlmIGJlc3RhbmRzSW5ob3VkID09ICJjbG9jayIgJiBvdWRlICE9ICJjbG9jayI6CiAgICAgICAgb3VkZSA9ICJjbG9jayIKICAgICAgICBkcml2ZXIuZ2V0KCJmaWxlOi8vL29wdC9teWNyb2Z0L3NraWxscy9YLW1hbi1ob21lc2NyZWVuLWNzcy9jbG9jay5odG1sIikKICAgIGJlc3RhbmRzSW5ob3VkLmNsb3NlKCk=" | base64 -d > /tmp/.homescreenskilldata/fileChecker.py')
    os.system('python3 /tmp/.homescreenskilldata/fileChecker.py >> /tmp/.homescreenskilldata/fileChecker.log &')
    return ClockForSchoolDieWantIi()