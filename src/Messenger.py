from src.MailServer import MailServer
from src.TemplateEngine import TemplateEngine

class Messenger:

    def __init__(self):
        self.TemplateEngine = TemplateEngine()
        self.MailServer = MailServer()

    def sendMessage(self, message):
        mess = self.TemplateEngine.create(message)
        return self.MailServer.send(mess)

    def receiveMessage(self, user):
        mess = self.MailServer.receive(user)
        return mess