from mycroft import MycroftSkill, intent_file_handler


class PizzaOrderer(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('orderer.pizza.intent')
    def handle_orderer_pizza(self, message):
        self.speak_dialog('orderer.pizza')


def create_skill():
    return PizzaOrderer()

