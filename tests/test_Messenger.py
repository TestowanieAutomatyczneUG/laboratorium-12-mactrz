from src.Messenger import Messenger
import unittest
from unittest.mock import MagicMock
from assertpy import assert_that


class TestMessenger(unittest.TestCase):

    def setUp(self):
        self.tmp = Messenger()

    def test_sendMessage_good(self):
        self.tmp.TemplateEngine.create = MagicMock(return_value='Message')
        self.tmp.MailServer.send = MagicMock(return_value=True)
        result = self.tmp.sendMessage('Message')
        assert_that(result).is_equal_to(True)

    def test_sendMessage_bad(self):
        self.tmp.TemplateEngine.create = MagicMock(return_value='Message')
        self.tmp.MailServer.send = MagicMock(return_value=False)
        result = self.tmp.sendMessage('Message')
        assert_that(result).is_equal_to(False)

    def test_receiveMessage_good(self):
        self.tmp.MailServer.receive = MagicMock(return_value='Message')
        result = self.tmp.receiveMessage(32)
        assert_that(result).is_equal_to('Message')

    def test_receiveMessage_bad(self):
        self.tmp.MailServer.receive = MagicMock(return_value=False)
        result = self.tmp.receiveMessage(32)
        assert_that(result).is_equal_to(False)