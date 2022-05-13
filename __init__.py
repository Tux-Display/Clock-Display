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
    os.system("rm -rf /tmp/.homescreenskilldata/page.txt 2>dev/null")
    os.system("touch /tmp/.homescreenskilldata/page.txt")
    os.system("echo \"homescreen\" > /tmp/.homescreenskilldata/page.txt")
    os.system('rm /tmp/.homescreenskilldata/fileChecker.py 2>/dev/null')
    os.system('touch /tmp/.homescreenskilldata/fileChecker.py')
    os.system('echo "IyEvYmluL3B5dGhvbjMKZnJvbSBzZWxlbml1bSBpbXBvcnQgd2ViZHJpdmVyCmZyb20gc2VsZW5pdW0ud2ViZHJpdmVyLmNocm9tZS5vcHRpb25zIGltcG9ydCBPcHRpb25zCmZyb20gd2ViZHJpdmVyX21hbmFnZXIuY2hyb21lIGltcG9ydCBDaHJvbWVEcml2ZXJNYW5hZ2VyCmltcG9ydCBvcwoKI2Nocm9tZSBicm93c2VyIHZvb3IgZGUga2xvawpjaHJvbWVfb3B0aW9ucyA9IE9wdGlvbnMoKQojIFZlcndpamRlcmQgaW5mb2JhcnMgLT4gYmFyIGRpZSBsaWV0IHdldGVuIGRhdCBoZXQgYXV0b21hdGVkIHdhcwpjaHJvbWVfb3B0aW9ucy5hZGRfZXhwZXJpbWVudGFsX29wdGlvbigidXNlQXV0b21hdGlvbkV4dGVuc2lvbiIsIEZhbHNlKQpjaHJvbWVfb3B0aW9ucy5hZGRfZXhwZXJpbWVudGFsX29wdGlvbigiZXhjbHVkZVN3aXRjaGVzIixbImVuYWJsZS1hdXRvbWF0aW9uIl0pCiMgY2hyb21lIGtpb3MgbW9kZSAtPiBnZWVuIGZ1bmN0aWVzIHpvZGF0IGRlIGdlYnJ1aWtlciBuaWtzIGthbiBkb2VuCiMgY2hyb21lX29wdGlvbnMuYWRkX2FyZ3VtZW50KCItLWtpb3NrIikKIyBjaHJvbWVfb3B0aW9ucy5hZGRfYXJndW1lbnQoIi0tZGlzYWJsZS1hcHBsaWNhdGlvbi1jYWNoZSIpCiMgY2hyb21lX29wdGlvbnMuYWRkX2FyZ3VtZW50KCJkaXNhYmxlLWluZm9iYXJzIikKZHJpdmVyID0gd2ViZHJpdmVyLkNocm9tZShvcHRpb25zPWNocm9tZV9vcHRpb25zKQojIG9wZW4gaG9tZSBwYWdpbmEKCgp3aGlsZSBUcnVlOgogICAgb3VkZSA9ICIiCiAgICAjIGRyaXZlci5nZXQoImZpbGU6Ly8vb3B0L215Y3JvZnQvc2tpbGxzL1gtbWFuLWhvbWVzY3JlZW4tY3NzL2hvbWVzY3JlZW4uaHRtbCIpCiAgICB3aXRoIG9wZW4oJy90bXAvLmhvbWVzY3JlZW5za2lsbGRhdGEvcGFnZS50eHQnKSBhcyBmOgogICAgICAgIGZpbGUgPSBmLnJlYWQoKQogICAgICAgIGlmIChmaWxlID09ICIiKToKICAgICAgICAgICAgb3VkZSA9ICJob21lc2NyZWVuIgogICAgICAgICAgICBkcml2ZXIuZ2V0KCJmaWxlOi8vL29wdC9teWNyb2Z0L3NraWxscy9YLW1hbi1ob21lc2NyZWVuLWNzcy9ob21lc2NyZWVuLmh0bWwiKQogICAgICAgIGlmKGZpbGUgPT0gImhvbWVzY3JlZW4iIGFuZCBvdWRlICE9ICJob21lc2NyZWVuIik6CiAgICAgICAgICAgIG91ZGUgPSAiaG9tZXNjcmVlbiIKICAgICAgICAgICAgZHJpdmVyLmdldCgiZmlsZTovLy9vcHQvbXljcm9mdC9za2lsbHMvWC1tYW4taG9tZXNjcmVlbi1jc3MvaG9tZXNjcmVlbi5odG1sIikKICAgICAgICBpZihmaWxlID09ICJjbG9jayIgYW5kIG91ZGUgIT0gImNsb2NrIik6CiAgICAgICAgICAgIG91ZGUgPSAiY2xvY2siCiAgICAgICAgICAgIGRyaXZlci5nZXQoImZpbGU6Ly8vb3B0L215Y3JvZnQvc2tpbGxzL1gtbWFuLWhvbWVzY3JlZW4tY3NzL2Nsb2NrLmh0bWwiKQ==" | base64 -d > /tmp/.homescreenskilldata/fileChecker.py')
    os.system('python3 /tmp/.homescreenskilldata/fileChecker.py >> /tmp/.homescreenskilldata/fileChecker.log &')
    return ClockForSchoolDieWantIi()