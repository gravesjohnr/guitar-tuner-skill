from mycroft import MycroftSkill, intent_file_handler


class GuitarTuner(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('tuner.guitar.intent')
    def handle_tuner_guitar(self, message):
        self.speak_dialog('tuner.guitar')


def create_skill():
    return GuitarTuner()

