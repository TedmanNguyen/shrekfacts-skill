from mycroft import MycroftSkill, intent_file_handler


class Shrekfacts(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('shrekfacts.intent')
    def handle_shrekfacts(self, message):
        self.speak_dialog('shrekfacts')


def create_skill():
    return Shrekfacts()

