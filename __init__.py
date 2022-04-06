from mycroft import MycroftSkill, intent_file_handler


class ClockForSchoolDieWantIi(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('ii.want.die.school.for.clock.intent')
    def handle_ii_want_die_school_for_clock(self, message):
        self.speak_dialog('ii.want.die.school.for.clock')
        print('test')


def create_skill():
    return ClockForSchoolDieWantIi()

